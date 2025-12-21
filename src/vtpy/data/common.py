"""Common data models and enums for VTube Studio API."""

from enum import Enum
from typing import Optional, Any, Dict, Literal
from pydantic import BaseModel, Field, ConfigDict

__all__ = [
    "API_NAME",
    "API_VERSION",
    "MessageType",
    "ErrorCode",
    "ErrorData",
    "BaseRequest",
    "BaseResponse",
    "BaseEvent",
    "HotkeyAction",
]

API_NAME = "VTubeStudioPublicAPI"
API_VERSION = "1.0"


class MessageType(str, Enum):
    """Message type identifiers for requests, responses, and events."""

    # Permissions
    PermissionRequest = "PermissionRequest"
    PermissionResponse = "PermissionResponse"

    # Authentication
    AuthenticationRequest = "AuthenticationRequest"
    AuthenticationResponse = "AuthenticationResponse"
    AuthenticationTokenRequest = "AuthenticationTokenRequest"
    AuthenticationTokenResponse = "AuthenticationTokenResponse"

    # Statistics
    StatisticsRequest = "StatisticsRequest"
    StatisticsResponse = "StatisticsResponse"

    # VTS Folder Info
    VTSFolderInfoRequest = "VTSFolderInfoRequest"
    VTSFolderInfoResponse = "VTSFolderInfoResponse"

    # Current Model
    CurrentModelRequest = "CurrentModelRequest"
    CurrentModelResponse = "CurrentModelResponse"
    ModelLoadRequest = "ModelLoadRequest"
    ModelLoadResponse = "ModelLoadResponse"
    MoveModelRequest = "MoveModelRequest"
    MoveModelResponse = "MoveModelResponse"
    HotkeyTriggerRequest = "HotkeyTriggerRequest"
    HotkeyTriggerResponse = "HotkeyTriggerResponse"
    HotkeysInCurrentModelRequest = "HotkeysInCurrentModelRequest"
    HotkeysInCurrentModelResponse = "HotkeysInCurrentModelResponse"

    # Available Models
    AvailableModelsRequest = "AvailableModelsRequest"
    AvailableModelsResponse = "AvailableModelsResponse"

    # Expression
    ExpressionStateRequest = "ExpressionStateRequest"
    ExpressionStateResponse = "ExpressionStateResponse"
    ExpressionActivationRequest = "ExpressionActivationRequest"
    ExpressionActivationResponse = "ExpressionActivationResponse"

    # Art Mesh
    ArtMeshListRequest = "ArtMeshListRequest"
    ArtMeshListResponse = "ArtMeshListResponse"
    ColorTintRequest = "ColorTintRequest"
    ColorTintResponse = "ColorTintResponse"
    ArtMeshSelectionRequest = "ArtMeshSelectionRequest"
    ArtMeshSelectionResponse = "ArtMeshSelectionResponse"
    SceneColorOverlayInfoRequest = "SceneColorOverlayInfoRequest"
    SceneColorOverlayInfoResponse = "SceneColorOverlayInfoResponse"
    FaceFoundRequest = "FaceFoundRequest"
    FaceFoundResponse = "FaceFoundResponse"
    InputParameterListRequest = "InputParameterListRequest"
    InputParameterListResponse = "InputParameterListResponse"
    ParameterValueRequest = "ParameterValueRequest"
    ParameterValueResponse = "ParameterValueResponse"
    Live2DParameterListRequest = "Live2DParameterListRequest"
    Live2DParameterListResponse = "Live2DParameterListResponse"
    ParameterCreationRequest = "ParameterCreationRequest"
    ParameterCreationResponse = "ParameterCreationResponse"
    ParameterDeletionRequest = "ParameterDeletionRequest"
    ParameterDeletionResponse = "ParameterDeletionResponse"
    InjectParameterDataRequest = "InjectParameterDataRequest"
    InjectParameterDataResponse = "InjectParameterDataResponse"

    # Item
    ItemListRequest = "ItemListRequest"
    ItemListResponse = "ItemListResponse"
    ItemLoadRequest = "ItemLoadRequest"
    ItemLoadResponse = "ItemLoadResponse"
    ItemUnloadRequest = "ItemUnloadRequest"
    ItemUnloadResponse = "ItemUnloadResponse"
    ItemAnimationControlRequest = "ItemAnimationControlRequest"
    ItemAnimationControlResponse = "ItemAnimationControlResponse"
    ItemMoveRequest = "ItemMoveRequest"
    ItemMoveResponse = "ItemMoveResponse"
    ItemSortRequest = "ItemSortRequest"
    ItemSortResponse = "ItemSortResponse"
    ItemPinRequest = "ItemPinRequest"
    ItemPinResponse = "ItemPinResponse"

    # Background
    SceneListRequest = "SceneListRequest"
    SceneListResponse = "SceneListResponse"
    CurrentSceneRequest = "CurrentSceneRequest"
    CurrentSceneResponse = "CurrentSceneResponse"
    SceneChangeRequest = "SceneChangeRequest"
    SceneChangeResponse = "SceneChangeResponse"

    # Physics
    GetCurrentModelPhysicsRequest = "GetCurrentModelPhysicsRequest"
    GetCurrentModelPhysicsResponse = "GetCurrentModelPhysicsResponse"
    SetCurrentModelPhysicsRequest = "SetCurrentModelPhysicsRequest"
    SetCurrentModelPhysicsResponse = "SetCurrentModelPhysicsResponse"

    # NDI
    NDIConfigRequest = "NDIConfigRequest"
    NDIConfigResponse = "NDIConfigResponse"

    # Post Processing
    PostProcessingListRequest = "PostProcessingListRequest"
    PostProcessingListResponse = "PostProcessingListResponse"
    PostProcessingUpdateRequest = "PostProcessingUpdateRequest"
    PostProcessingUpdateResponse = "PostProcessingUpdateResponse"

    # Event Subscription
    EventSubscriptionRequest = "EventSubscriptionRequest"
    EventSubscriptionResponse = "EventSubscriptionResponse"


class ErrorCode(int, Enum):
    """Error codes returned by VTube Studio API."""

    # Success
    None_ = 0

    # General errors
    InvalidRequest = 1
    RequestedItemNotFound = 2
    MissingParameterInRequest = 3
    RequestedItemIsDeactivated = 4
    RequestedItemIsAlreadyInThatState = 5
    GenericError = 6

    # Authentication errors
    AuthenticationTokenMissing = 100
    AuthenticationTokenInvalid = 101
    AuthenticationTokenRequestDenied = 102
    AuthenticationTokenRequestTimedOut = 103
    AuthenticationTokenRequestAlreadyHandled = 104

    # Model errors
    ModelNotFound = 200
    ModelFileInvalid = 201
    ModelAlreadyLoaded = 202
    ModelLoadTimedOut = 203
    ModelLoadCancelled = 204
    ModelLoadFailed = 205

    # Hotkey errors
    HotkeyNotFound = 300
    HotkeyTriggerFailed = 301

    # Expression errors
    ExpressionNotFound = 400
    ExpressionActivationFailed = 401

    # Art mesh errors
    ArtMeshNotFound = 500
    ColorTintFailed = 501

    # Item errors
    ItemNotFound = 600
    ItemLoadFailed = 601
    ItemUnloadFailed = 602
    ItemAnimationNotFound = 603
    ItemAnimationFailed = 604

    # Scene errors
    SceneNotFound = 700
    SceneChangeFailed = 701

    # NDI errors
    NDINotAvailable = 800
    NDIConfigFailed = 801


class ErrorData(BaseModel):
    """Error data returned in API responses."""

    errorID: ErrorCode
    message: str

    model_config = ConfigDict(use_enum_values=True)


class BaseRequest(BaseModel):
    """Base class for all API requests."""

    apiName: Literal[API_NAME] = API_NAME
    apiVersion: Literal[API_VERSION] = API_VERSION
    requestID: Optional[str] = None

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


class BaseResponse(BaseModel):
    """Base class for all API responses."""

    apiName: Literal[API_NAME] = API_NAME
    apiVersion: Literal[API_VERSION] = API_VERSION
    timestamp: int
    requestID: Optional[str] = None

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


class BaseEvent(BaseModel):
    """Base class for all API events."""

    apiName: Literal[API_NAME] = API_NAME
    apiVersion: Literal[API_VERSION] = API_VERSION
    timestamp: int
    requestID: Optional[str] = None

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


class HotkeyAction(Enum):
    Unset = -1  # Unset.
    TriggerAnimation = 0  # Play an animation.
    ChangeIdleAnimation = 1  # Change the idle animation.
    ToggleExpression = 2  # Toggle an expression.
    RemoveAllExpressions = 3  # Remove all expressions.
    MoveModel = 4  # Moves the model to the target position.
    ChangeBackground = 5  # Change the current background.
    ReloadMicrophone = 6  # Reload the current microphone.
    ReloadTextures = 7  # Reload the model texture.
    CalibrateCam = 8  # Calibrate Camera.
    ChangeVTSModel = 9  # Change VTS Model.
    TakeScreenshot = 10  # Take a screenshot with the previous settings.
    ScreenColorOverlay = 11  # Activates/Deactivates model screen color overlay.
    RemoveAllItems = 12  # Removes all items from the scene.
    ToggleItemScene = 13  # Loads an item scene.
    DownloadRandomWorkshopItem = 14  # Downloads a random item from the Steam Workshop and attempts to load it into the scene.
    ExecuteItemAction = 15  # Executes a hotkey in the given Live2D item.
    ArtMeshColorPreset = 16  # Loads the recorded ArtMesh multiply/screen color preset.
    ToggleTracker = 17  # Toggles the tracking on/off. Can be webcam or USB/WiFi connected phone.
    ToggleTwitchFeature = 18  # Toggles a Twitch feature (for example Emote Dropper) on/off.
    LoadEffectPreset = 19  # Loads post processing effect preset.
    ToggleLive2DEditorAPI = 20  # Toggles Live2D Editor API parameter sync on/off.
    WebItemAction = 21  # Triggers Web Item action.
