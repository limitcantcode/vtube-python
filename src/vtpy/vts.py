"""VTS class for managing WebSocket connection and API interactions with VTube Studio."""

import asyncio
import json
import logging
import uuid
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Union,
    Awaitable,
)
from websockets.asyncio.client import ClientConnection, connect
from websockets.exceptions import ConnectionClosed

from vtpy.data.common import *
from vtpy.data.requests import *
from vtpy.data.events import *
from vtpy.error import VTSRequestError

logger = logging.getLogger(__name__)


class VTS:
    """Main class for interacting with VTube Studio via WebSocket API.

    This class manages the WebSocket connection, handles authentication,
    and provides an event-driven interface for subscribing to VTube Studio events.

    Example:
        ```python
        vts = VTS(plugin_name="MyPlugin", plugin_developer="Developer")
        await vts.start(host="localhost", port=8001, auth_token="your_token")

        # Register event handler
        async def on_model_loaded(event: ModelLoadedEvent):
            print(f"Model loaded: {event.data.modelName}")

        vts.on_event(EventType.ModelLoadedEvent, on_model_loaded)
        ```
    """

    def __init__(
        self,
        plugin_name: str,
        plugin_developer: str,
        plugin_icon: Optional[str] = None,
    ):
        """Initialize VTS client.

        Args:
            plugin_name: Name of your plugin
            plugin_developer: Developer name
            plugin_icon: Optional base64 encoded icon (not used in current implementation)
        """
        self.plugin_name = plugin_name
        self.plugin_developer = plugin_developer
        self.plugin_icon = plugin_icon

        # Connection state
        self._ws: Optional[ClientConnection] = None
        self._connected: bool = False
        self._authenticated: bool = False
        self._host: Optional[str] = None
        self._port: Optional[int] = None
        self._auth_token: Optional[str] = None

        # Request/response tracking
        self._pending_requests: Dict[str, asyncio.Future] = {}
        self._request_counter: int = 0

        # Event handlers - stored as lists per event type
        self._event_handlers: Dict[EventType, List[Callable[[BaseEvent], Awaitable[None]]]] = {}

        # Background task for receiving messages
        self._receive_task: Optional[asyncio.Task] = None

        # Async event handling
        self._handler_processing_task: Optional[asyncio.Task] = None
        self._handler_processing_queue: asyncio.Queue = asyncio.Queue()

    @property
    def connected(self) -> bool:
        """Check if connected to VTube Studio."""
        return self._connected

    @property
    def authenticated(self) -> bool:
        """Check if authenticated with VTube Studio."""
        return self._authenticated

    async def start(
        self,
        host: str = "localhost",
        port: int = 8001,
        auth_token: Optional[str] = None,
        auth_file: Union[str, Path] = "vts_token.txt",
        save_auth_token: bool = True,
    ) -> str:
        """Connect to VTube Studio and authenticate.

        Args:
            host: VTube Studio WebSocket host (default: "localhost")
            port: VTube Studio WebSocket port (default: 8001)
            auth_token: Authentication token as string, Path to token file, or None to request new token

        Returns:
            Authentication token string

        Raises:
            ConnectionError: If connection fails
            ValueError: If authentication fails
        """

        if self._connected:
            raise ConnectionError("Already connected to a VTube Studio instance")

        self._host = host
        self._port = port

        # Connect WebSocket
        uri = f"ws://{host}:{port}"
        logger.info(f"Connecting to VTube Studio at {uri}")
        try:
            self._ws = await connect(uri)
            self._connected = True
        except Exception as e:
            logger.error(f"Failed to connect to VTube Studio: {e}", exc_info=True)
            raise ConnectionError(f"Failed to connect to VTube Studio: {e}") from e

        # Start async processors
        self._receive_task = asyncio.create_task(self._receive_loop())
        self._handler_processing_task = asyncio.create_task(self._handler_processing_loop())

        try:
            # Handles provided auth_file
            if isinstance(auth_file, str):
                auth_file = Path(auth_file)
            if isinstance(auth_file, Path):
                auth_file.mkdir(parents=True, exist_ok=True)
            if auth_file and auth_file.is_file():
                with open(auth_file, "r") as f:
                    auth_token = f.read().strip()

            # Attempt authentication using existing auth_token
            if auth_token:
                try:
                    return await self._authenticate(
                        auth_token=auth_token, auth_file=auth_file, save_auth_token=save_auth_token
                    )
                except ValueError as e:
                    logger.error(f"Failed to authenticate using existing token: {e}", exc_info=True)
                    logger.info("Getting a new token")

            # Request new token
            auth_token = await self._request_authentication_token()

            # Authenticate with new token
            return await self._authenticate(
                auth_token=auth_token, auth_file=auth_file, save_auth_token=save_auth_token
            )

        except Exception as e:
            logger.error(f"Failed to connect to VTube Studio: {e}", exc_info=True)
            await self.close()
            raise ConnectionError(f"Failed to connect to VTube Studio: {e}") from e

    async def _request_authentication_token(self) -> str:
        """Request a new authentication token from VTube Studio.

        Args:
            host: VTube Studio WebSocket host
            port: VTube Studio WebSocket port

        Returns:
            Authentication token string

        Raises:
            ConnectionError: If unable to request token
            ValueError: If token request fails
        """
        # Send token request
        response = await self.request_authentication_token(
            AuthenticationTokenRequestData(
                pluginName=self.plugin_name,
                pluginDeveloper=self.plugin_developer,
                pluginIcon=self.plugin_icon,
            )
        )

        # Check for errors
        if isinstance(response.data, ErrorData):
            error_msg = f"Token request failed: {response.data.message}"
            logger.error(error_msg, exc_info=True)
            raise ValueError(error_msg)

        token = response.data.authenticationToken
        logger.info("Successfully obtained authentication token")
        return token

    async def _authenticate(
        self,
        auth_token: str = None,
        auth_file: Optional[Union[Path]] = None,
        save_auth_token: bool = True,
    ) -> None:
        """Authenticate with VTube Studio using the stored token.

        Raises:
            ValueError: If authentication fails
        """
        if not auth_token:
            auth_token = self._auth_token
        if not auth_token:
            raise ValueError("No authentication token available")

        response = await self.request_authentication(
            AuthenticationRequestData(
                pluginName=self.plugin_name,
                pluginDeveloper=self.plugin_developer,
                authenticationToken=auth_token,
            ),
        )

        if isinstance(response.data, ErrorData):
            error_msg = f"Authentication failed: {response.data.message}"
            logger.error(error_msg, exc_info=True)
            raise ValueError(error_msg)

        if not response.data.authenticated:
            reason = response.data.reason or "Unknown reason"
            error_msg = f"Authentication failed: {reason}"
            logger.error(error_msg, exc_info=True)
            raise ValueError(error_msg)

        self._auth_token = auth_token
        if save_auth_token and isinstance(auth_file, Path):
            with open(auth_file, "w") as f:
                f.write(auth_token)
            logger.info(f"Saved authentication token to {auth_file}")

        self._authenticated = True
        logger.info("Successfully authenticated with VTube Studio")

        return auth_token

    async def close(self) -> None:
        """Close the WebSocket connection."""
        if self._receive_task:
            self._receive_task.cancel()
            try:
                await self._receive_task
            except asyncio.CancelledError:
                pass

        if self._handler_processing_task:
            self._handler_processing_task.cancel()
            try:
                await self._handler_processing_task
            except asyncio.CancelledError:
                pass

        if self._ws:
            await self._ws.close()
            self._ws = None

        for request_id, future in self._pending_requests.items():
            if not future.done():
                future.set_exception(ConnectionError("Connection closed"))

        self._connected = False
        self._authenticated = False
        self._auth_token = None
        logger.info("Disconnected from VTube Studio")

    def generate_request_id(self) -> str:
        """Generate a unique request ID.

        Returns:
            A unique request ID string
        """
        self._request_counter += 1
        return f"{self._request_counter}_{uuid.uuid4().hex[:8]}"

    async def _send_request(
        self,
        request: BaseRequest,
        response_type: type[BaseResponse],
        timeout: float = 30.0,
    ) -> BaseResponse:
        """Send a request and wait for the response.

        Args:
            request: The request to send
            response_type: Expected response type
            timeout: Timeout in seconds

        Returns:
            The response object

        Raises:
            ConnectionError: If not connected
            TimeoutError: If response times out
            ValueError: If response is invalid
        """
        if not self._connected or not self._ws:
            raise ConnectionError("Not connected to VTube Studio")

        # Generate request ID if not set
        if not request.requestID:
            request.requestID = self.generate_request_id()

        request_id = request.requestID

        # Create future for response
        future = asyncio.Future()
        self._pending_requests[request_id] = future

        try:
            # Send request
            await self._ws.send(request.model_dump_json(exclude_none=True))

            # Wait for response
            try:
                response_data = await asyncio.wait_for(future, timeout=timeout)
            except asyncio.TimeoutError:
                self._pending_requests.pop(request_id, None)
                raise TimeoutError(f"Request {request_id} timed out after {timeout}s")

            # Parse response
            response = response_type.model_validate(response_data)
            return response

        finally:
            self._pending_requests.pop(request_id, None)

    async def _receive_loop(self) -> None:
        """Background task to receive and process messages from WebSocket."""
        if not self._ws:
            return

        try:
            async for message in self._ws:
                try:
                    await self._handle_message(message)
                except Exception as e:
                    logger.error(f"Error handling message: {e}", exc_info=True)
        except asyncio.CancelledError:
            pass
        except ConnectionClosed:
            logger.info("WebSocket connection closed")
            await self.close()
        except Exception as e:
            logger.error(f"Error in receive loop: {e}", exc_info=True)
            await self.close()

    async def _handler_processing_loop(self) -> None:
        """Background task to process event handlers."""
        while True:
            try:
                handlers_to_process: List[Awaitable] = list()
                handlers_to_process.append(await self._handler_processing_queue.get())
                while not self._handler_processing_queue.empty():
                    handlers_to_process.append(await self._handler_processing_queue.get())
                results = await asyncio.gather(*handlers_to_process, return_exceptions=True)
                for result in results:
                    if isinstance(result, Exception):
                        logger.error(f"Error processing handler: {result}", exc_info=True)
                    else:
                        logger.debug(f"Handler processed: {result}")
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in handler processing loop: {e}", exc_info=True)

    async def _handle_message(self, message: Union[str, bytes]) -> None:
        """Handle incoming message from WebSocket.

        Args:
            message: Raw message from WebSocket
        """
        if isinstance(message, bytes):
            message = message.decode("utf-8")

        data = json.loads(message)

        request_id = data.get("requestID")
        if request_id and request_id in self._pending_requests:
            future = self._pending_requests[request_id]
            if not future.done():
                future.set_result(data)
            return

        message_type = data.get("messageType")
        if message_type and message_type in EventType:
            await self._handle_event(data)
            return

        # Unknown message type
        logger.warning(f"Received unknown message type: {data}")

    async def _handle_event(self, event_data: Dict[str, Any]) -> None:
        """Handle an incoming event and dispatch to all registered handlers.

        Args:
            event_data: Raw event data from WebSocket
        """
        try:
            # Check for eventName first, then messageType (some events use messageType)
            event_name_str = event_data.get("messageType")
            if not event_name_str:
                logger.warning(f"Event missing eventName/messageType: {event_data}")
                return

            # Map event name to EventType enum
            event_type = EventType(event_name_str)

            # Get corresponding model class
            event_model_class = EVENT_MODEL_MAP[event_type]

            # Parse event using Pydantic
            # TODO: Figure out why send_message works but not this and requires this patch
            event_data["messageType"] = event_type
            event = event_model_class.model_validate(event_data)

            # Dispatch to all handlers
            handlers = self._event_handlers.get(event_type, [])
            for handler in handlers:
                await self._handler_processing_queue.put(handler(event))
        except Exception as e:
            logger.error(f"Error handling event: {e}", exc_info=True)

    def on_event(
        self,
        event_type: EventType,
        handler: Callable[[BaseEvent], Awaitable[None]],
    ) -> None:
        """Register an event handler for a specific event type.

        Args:
            event_type: The type of event to listen for
            handler: Async function that will be called when the event occurs.
                    The function should accept one parameter (the event object).

        Example:
            ```python
            async def on_model_loaded(event: ModelLoadedEvent):
                print(f"Model loaded: {event.data.modelName}")

            vts.on_event(EventType.ModelLoadedEvent, on_model_loaded)
            ```
        """
        if event_type not in self._event_handlers:
            self._event_handlers[event_type] = list()

        self._event_handlers[event_type].append(handler)
        logger.debug(f"Registered handler for {event_type}")

    def remove_event_handler(
        self,
        event_type: EventType,
        handler: Callable[[BaseEvent], Awaitable[None]],
    ) -> None:
        """Remove an event handler.

        Args:
            event_type: The event type
            handler: The handler function to remove

        Raises:
            ValueError: If handler is not registered
        """
        if event_type not in self._event_handlers:
            raise ValueError(f"No handlers registered for {event_type}")

        if handler not in self._event_handlers[event_type]:
            raise ValueError("Handler not found")

        self._event_handlers[event_type].remove(handler)
        logger.debug(f"Removed handler for {event_type}")

    async def event_sub_test(
        self, data: TestEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = TestEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def event_sub_model_loaded(
        self, data: ModelLoadedEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = ModelLoadedEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def event_sub_tracking_status_changed(
        self, data: TrackingStatusChangedEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = TrackingStatusChangedEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def event_sub_background_changed(
        self, data: BackgroundChangedEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = BackgroundChangedEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def event_sub_model_config_modified(
        self, data: ModelConfigChangedEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = ModelConfigChangedEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def event_sub_model_moved(
        self, data: ModelMovedEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = ModelMovedEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def event_sub_model_outline(
        self, data: ModelOutlineEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = ModelOutlineEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def event_sub_hotkey_triggered(
        self, data: HotkeyTriggeredEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = HotkeyTriggeredEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def event_sub_model_animation(
        self, data: ModelAnimationEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = ModelAnimationEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def event_sub_item(
        self, data: ItemEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = ItemEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def event_sub_model_clicked(
        self, data: ModelClickedEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = ModelClickedEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def event_sub_post_processing(
        self, data: PostProcessingEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = PostProcessingEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def event_sub_live2d_cubism_editor_connected(
        self, data: Live2DCubismEditorConnectedEventSubscriptionRequestData
    ) -> EventSubscriptionResponse:
        request = Live2DCubismEditorConnectedEventSubscriptionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        return await self._send_request(request, EventSubscriptionResponse)

    async def request_permission(self, permission: PermissionRequestData) -> PermissionResponse:
        request = PermissionRequest(
            requestID=self.generate_request_id(),
            data=permission,
        )
        response = await self._send_request(request, PermissionResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_authentication(
        self, data: AuthenticationRequestData
    ) -> AuthenticationResponse:
        request = AuthenticationRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, AuthenticationResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_authentication_token(
        self, data: AuthenticationTokenRequestData
    ) -> AuthenticationTokenResponse:
        request = AuthenticationTokenRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, AuthenticationTokenResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_statistics(self, data: StatisticsRequestData) -> StatisticsResponse:
        request = StatisticsRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, StatisticsResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_vts_folder_info(
        self, data: VTSFolderInfoRequestData
    ) -> VTSFolderInfoResponse:
        request = VTSFolderInfoRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, VTSFolderInfoResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_current_model(self, data: CurrentModelRequestData) -> CurrentModelResponse:
        request = CurrentModelRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, CurrentModelResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_available_models(
        self, data: AvailableModelsRequestData
    ) -> AvailableModelsResponse:
        request = AvailableModelsRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, AvailableModelsResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_model_load(
        self, data: ModelLoadRequestRequestData
    ) -> ModelLoadRequestResponse:
        request = ModelLoadRequestRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ModelLoadRequestResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_move_model(self, data: MoveModelRequestData) -> MoveModelResponse:
        request = MoveModelRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, MoveModelResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_hotkeys_in_current_model(
        self, data: HotkeysInCurrentModelRequestData
    ) -> HotkeysInCurrentModelResponse:
        request = HotkeysInCurrentModelRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, HotkeysInCurrentModelResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_hotkey_trigger(self, data: HotkeyTriggerRequestData) -> HotkeyTriggerResponse:
        request = HotkeyTriggerRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, HotkeyTriggerResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_expression_state(
        self, data: ExpressionStateRequestData
    ) -> ExpressionStateResponse:
        request = ExpressionStateRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ExpressionStateResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_expression_activation(
        self, data: ExpressionActivationRequestData
    ) -> ExpressionActivationResponse:
        request = ExpressionActivationRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ExpressionActivationResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_art_mesh_list(self, data: ArtMeshListRequestData) -> ArtMeshListResponse:
        request = ArtMeshListRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ArtMeshListResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_color_tint(self, data: ColorTintRequestData) -> ColorTintResponse:
        request = ColorTintRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ColorTintResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_scene_color_overlay_info(
        self, data: SceneColorOverlayInfoRequestData
    ) -> SceneColorOverlayInfoResponse:
        request = SceneColorOverlayInfoRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, SceneColorOverlayInfoResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_face_found(self, data: FaceFoundRequestData) -> FaceFoundResponse:
        request = FaceFoundRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, FaceFoundResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_input_parameter_list(
        self, data: InputParameterListRequestData
    ) -> InputParameterListResponse:
        request = InputParameterListRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, InputParameterListResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_parameter_value(
        self, data: ParameterValueRequestData
    ) -> ParameterValueResponse:
        request = ParameterValueRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ParameterValueResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_live2d_parameter_list(
        self, data: Live2DParameterListRequestData
    ) -> Live2DParameterListResponse:
        request = Live2DParameterListRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, Live2DParameterListResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_parameter_creation(
        self, data: ParameterCreationRequestData
    ) -> ParameterCreationResponse:
        request = ParameterCreationRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ParameterCreationResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_parameter_deletion(
        self, data: ParameterDeletionRequestData
    ) -> ParameterDeletionResponse:
        request = ParameterDeletionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ParameterDeletionResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_inject_parameter_data(
        self, data: InjectParameterDataRequestData
    ) -> InjectParameterDataResponse:
        request = InjectParameterDataRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, InjectParameterDataResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_get_current_model_physics(
        self, data: GetCurrentModelPhysicsRequestData
    ) -> GetCurrentModelPhysicsResponse:
        request = GetCurrentModelPhysicsRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, GetCurrentModelPhysicsResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_set_current_model_physics(
        self, data: SetCurrentModelPhysicsRequestData
    ) -> SetCurrentModelPhysicsResponse:
        request = SetCurrentModelPhysicsRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, SetCurrentModelPhysicsResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_ndi_config(self, data: NDIConfigRequestData) -> NDIConfigResponse:
        request = NDIConfigRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, NDIConfigResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_item_list(self, data: ItemListRequestData) -> ItemListResponse:
        request = ItemListRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ItemListResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_item_load(self, data: ItemLoadRequestData) -> ItemLoadResponse:
        request = ItemLoadRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ItemLoadResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_item_unload(self, data: ItemUnloadRequestData) -> ItemUnloadResponse:
        request = ItemUnloadRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ItemUnloadResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_item_animation_control(
        self, data: ItemAnimationControlRequestData
    ) -> ItemAnimationControlResponse:
        request = ItemAnimationControlRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ItemAnimationControlResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_item_move(self, data: ItemMoveRequestData) -> ItemMoveResponse:
        request = ItemMoveRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ItemMoveResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_item_sort(self, data: ItemSortRequestData) -> ItemSortResponse:
        request = ItemSortRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ItemSortResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_art_mesh_selection(
        self, data: ArtMeshSelectionRequestData
    ) -> ArtMeshSelectionResponse:
        request = ArtMeshSelectionRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ArtMeshSelectionResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_item_pin(self, data: ItemPinRequestData) -> ItemPinResponse:
        request = ItemPinRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, ItemPinResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_post_processing_list(
        self, data: PostProcessingListRequestData
    ) -> PostProcessingListResponse:
        request = PostProcessingListRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, PostProcessingListResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response

    async def request_post_processing_update(
        self, data: PostProcessingUpdateRequestData
    ) -> PostProcessingUpdateResponse:
        request = PostProcessingUpdateRequest(
            requestID=self.generate_request_id(),
            data=data,
        )
        response = await self._send_request(request, PostProcessingUpdateResponse)
        if isinstance(response.data, ErrorData):
            raise VTSRequestError(response.data.message, response.data.errorID)
        return response
