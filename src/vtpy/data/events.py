"""Event data models for VTube Studio API."""

# TODO:
# - make event configs fields optional
# - document fields
# - replace type str for path where appropriate
# - check for enums in API docs

from ast import Str
from typing import Optional, List, Dict, Any, Literal, Union
from enum import Enum
from pydantic import BaseModel, Field
from vtpy.data.common import (
    BaseRequest,
    BaseResponse,
    BaseEvent,
    ErrorData,
    MessageType,
    HotkeyAction,
)

__all__ = [
    "EventType",
    "EVENT_MODEL_MAP",
    "WindowSize",
    "AnimationEventType",
    "ItemEventType",
    "BaseEventSubscriptionRequest",
    "EventSubscriptionResponseData",
    "EventSubscriptionResponse",
    "MouseButtonID",
    "TestEventSubscriptionRequestConfig",
    "TestEventSubscriptionRequestData",
    "TestEventSubscriptionRequest",
    "TestEventData",
    "TestEvent",
    "ModelLoadedEventSubscriptionRequestConfig",
    "ModelLoadedEventSubscriptionRequestData",
    "ModelLoadedEventSubscriptionRequest",
    "ModelLoadedEventData",
    "ModelLoadedEvent",
    "TrackingStatusChangedEventSubscriptionRequestConfig",
    "TrackingStatusChangedEventSubscriptionRequestData",
    "TrackingStatusChangedEventSubscriptionRequest",
    "TrackingStatusChangedEventData",
    "TrackingStatusChangedEvent",
    "BackgroundChangedEventSubscriptionRequestConfig",
    "BackgroundChangedEventSubscriptionRequestData",
    "BackgroundChangedEventSubscriptionRequest",
    "BackgroundChangedEventData",
    "BackgroundChangedEvent",
    "ModelConfigChangedEventSubscriptionRequestConfig",
    "ModelConfigChangedEventSubscriptionRequestData",
    "ModelConfigChangedEventSubscriptionRequest",
    "ModelConfigChangedEventData",
    "ModelConfigChangedEvent",
    "ModelMovedEventSubscriptionRequestConfig",
    "ModelMovedEventSubscriptionRequestData",
    "ModelMovedEventSubscriptionRequest",
    "ModelPositionData",
    "ModelMovedEventData",
    "ModelMovedEvent",
    "ModelOutlineEventSubscriptionRequestConfig",
    "ModelOutlineEventSubscriptionRequestData",
    "ModelOutlineEventSubscriptionRequest",
    "ConvexHullPoint",
    "ModelOutlineEventData",
    "ModelOutlineEvent",
    "HotkeyTriggeredEventSubscriptionRequestConfig",
    "HotkeyTriggeredEventSubscriptionRequestData",
    "HotkeyTriggeredEventSubscriptionRequest",
    "HotkeyTriggeredEventData",
    "HotkeyTriggeredEvent",
    "ModelAnimationEventSubscriptionRequestConfig",
    "ModelAnimationEventSubscriptionRequestData",
    "ModelAnimationEventSubscriptionRequest",
    "ModelAnimationEventData",
    "ModelAnimationEvent",
    "ItemEventSubscriptionRequestConfig",
    "ItemEventSubscriptionRequestData",
    "ItemEventSubscriptionRequest",
    "ItemPosition",
    "ItemEventData",
    "ItemEvent",
    "ModelClickedEventSubscriptionRequestConfig",
    "ModelClickedEventSubscriptionRequestData",
    "ModelClickedEventSubscriptionRequest",
    "HitInfo",
    "ArtMeshHit",
    "ClickPosition",
    "ModelClickedEventData",
    "ModelClickedEvent",
    "PostProcessingEventSubscriptionRequestConfig",
    "PostProcessingEventSubscriptionRequestData",
    "PostProcessingEventSubscriptionRequest",
    "PostProcessingEventData",
    "PostProcessingEvent",
    "Live2DCubismEditorConnectedEventSubscriptionRequestConfig",
    "Live2DCubismEditorConnectedEventSubscriptionRequestData",
    "Live2DCubismEditorConnectedEventSubscriptionRequest",
    "Live2DCubismEditorConnectedEventData",
    "Live2DCubismEditorConnectedEvent",
]
# ============================================================================
# Event Types
# ============================================================================


class EventType(Enum):
    """Event type identifiers."""

    TestEvent = "TestEvent"
    ModelLoadedEvent = "ModelLoadedEvent"
    TrackingStatusChangedEvent = "TrackingStatusChangedEvent"
    BackgroundChangedEvent = "BackgroundChangedEvent"
    ModelConfigChangedEvent = "ModelConfigChangedEvent"
    ModelMovedEvent = "ModelMovedEvent"
    ModelOutlineEvent = "ModelOutlineEvent"
    HotkeyTriggeredEvent = "HotkeyTriggeredEvent"
    ModelAnimationEvent = "ModelAnimationEvent"
    ItemEvent = "ItemEvent"
    ModelClickedEvent = "ModelClickedEvent"
    PostProcessingEvent = "PostProcessingEvent"
    Live2DCubismEditorConnectedEvent = "Live2DCubismEditorConnectedEvent"


class AnimationEventType(Enum):
    Custom = "Custom"
    Start = "Start"
    End = "End"


class ItemEventType(Enum):
    Added = "Added"
    Removed = "Removed"
    DroppedPinned = "DroppedPinned"
    DroppedUnpinned = "DroppedUnpinned"
    Clicked = "Clicked"
    Locked = "Locked"
    Unlocked = "Unlocked"


# ============================================================================
# Helper Types
# ============================================================================


class WindowSize(BaseModel):
    x: float
    y: float


# ============================================================================
# Event Sub
# ============================================================================


class BaseEventSubscriptionRequest(BaseRequest):
    """Request to subscribe to events."""

    messageType: Literal[MessageType.EventSubscriptionRequest] = (
        MessageType.EventSubscriptionRequest
    )


class EventSubscriptionResponseData(BaseModel):
    """Data for event subscription response."""

    subscribedEventCount: int
    subscribedEvents: List[EventType]


class EventSubscriptionResponse(BaseResponse):
    """Response from event subscription request."""

    messageType: Literal[MessageType.EventSubscriptionResponse] = (
        MessageType.EventSubscriptionResponse
    )
    data: Union[EventSubscriptionResponseData, ErrorData]


class MouseButtonID(Enum):
    Left = 0
    Right = 1
    Middle = 2


# ============================================================================
# Test Events
# ============================================================================


class TestEventSubscriptionRequestConfig(BaseModel):
    """Config for test event subscription request."""

    testMessageForEvent: Optional[str] = Field(
        None, description="Test message returned in the event."
    )


class TestEventSubscriptionRequestData(BaseModel):
    """Config for test event subscription request."""

    eventName: Literal[EventType.TestEvent] = EventType.TestEvent
    subscribe: bool = True
    config: TestEventSubscriptionRequestConfig


class TestEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: TestEventSubscriptionRequestData


class TestEventData(BaseModel):
    """Data for model loaded event."""

    yourTestMessage: str = Field(description="Test message returned in the event.")
    counter: int = Field(description="Counter of the event.")


class TestEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.TestEvent] = EventType.TestEvent
    data: TestEventData


# ============================================================================
# Model Events
# ============================================================================


class ModelLoadedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""

    modelID: Optional[List[str]] = Field(None, description="The ID of the model to listen for.")


class ModelLoadedEventSubscriptionRequestData(BaseModel):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ModelLoadedEvent] = EventType.ModelLoadedEvent
    subscribe: bool = True
    config: ModelLoadedEventSubscriptionRequestConfig


class ModelLoadedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: ModelLoadedEventSubscriptionRequestData


class ModelLoadedEventData(BaseModel):
    """Data for model loaded event."""

    modelLoaded: bool
    modelName: str
    modelID: str


class ModelLoadedEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.ModelLoadedEvent] = EventType.ModelLoadedEvent
    data: ModelLoadedEventData


# ============================================================================
# Tracking Events
# ============================================================================


class TrackingStatusChangedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""


class TrackingStatusChangedEventSubscriptionRequestData(BaseModel):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.TrackingStatusChangedEvent] = EventType.TrackingStatusChangedEvent
    subscribe: bool = True
    config: TrackingStatusChangedEventSubscriptionRequestConfig


class TrackingStatusChangedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: TrackingStatusChangedEventSubscriptionRequestData


class TrackingStatusChangedEventData(BaseModel):
    """Data for model loaded event."""

    faceFound: bool
    leftHandFound: bool
    rightHandFound: bool


class TrackingStatusChangedEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.TrackingStatusChangedEvent] = (
        EventType.TrackingStatusChangedEvent
    )
    data: TrackingStatusChangedEventData


# ============================================================================
# Background Events
# ============================================================================


class BackgroundChangedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""


class BackgroundChangedEventSubscriptionRequestData(BaseModel):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.BackgroundChangedEvent] = EventType.BackgroundChangedEvent
    subscribe: bool = True
    config: BackgroundChangedEventSubscriptionRequestConfig


class BackgroundChangedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: BackgroundChangedEventSubscriptionRequestData


class BackgroundChangedEventData(BaseModel):
    """Data for model loaded event."""

    backgroundName: str


class BackgroundChangedEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.BackgroundChangedEvent] = EventType.BackgroundChangedEvent
    data: BackgroundChangedEventData


# ============================================================================
# Model Config Events
# ============================================================================


class ModelConfigChangedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""


class ModelConfigChangedEventSubscriptionRequestData(BaseModel):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ModelConfigChangedEvent] = EventType.ModelConfigChangedEvent
    subscribe: bool = True
    config: ModelConfigChangedEventSubscriptionRequestConfig


class ModelConfigChangedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: ModelConfigChangedEventSubscriptionRequestData


class ModelConfigChangedEventData(BaseModel):
    """Data for model loaded event."""

    modelID: str
    modelName: str
    hotkeyConfigChanged: bool


class ModelConfigChangedEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.ModelConfigChangedEvent] = EventType.ModelConfigChangedEvent
    data: ModelConfigChangedEventData


# ============================================================================
# Model Moved Events
# ============================================================================


class ModelMovedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""


class ModelMovedEventSubscriptionRequestData(BaseModel):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ModelMovedEvent] = EventType.ModelMovedEvent
    subscribe: bool = True
    config: ModelMovedEventSubscriptionRequestConfig


class ModelMovedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: ModelMovedEventSubscriptionRequestData


class ModelPositionData(BaseModel):
    """Data for model position."""

    positionX: float
    positionY: float
    rotation: float
    size: float


class ModelMovedEventData(BaseModel):
    """Data for model loaded event."""

    modelID: str
    modelName: str
    modelPosition: ModelPositionData


class ModelMovedEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.ModelMovedEvent] = EventType.ModelMovedEvent
    data: ModelMovedEventData


# ============================================================================
# Model Outline Events
# ============================================================================


class ModelOutlineEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""

    draw: Optional[bool] = Field(None, description="Whether to draw the model outline.")


class ModelOutlineEventSubscriptionRequestData(BaseModel):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ModelOutlineEvent] = EventType.ModelOutlineEvent
    subscribe: bool = True
    config: ModelOutlineEventSubscriptionRequestConfig


class ModelOutlineEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: ModelOutlineEventSubscriptionRequestData


class ConvexHullPoint(BaseModel):
    x: float
    y: float


class ModelOutlineEventData(BaseModel):
    """Data for model loaded event."""

    modelID: str
    modelName: str
    convexHull: List[ConvexHullPoint]
    convexHullCenter: ConvexHullPoint
    windowSize: WindowSize


class ModelOutlineEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.ModelOutlineEvent] = EventType.ModelOutlineEvent
    data: ModelOutlineEventData


# ============================================================================
# Hotkey Events
# ============================================================================


class HotkeyTriggeredEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""

    onlyForAction: Optional[HotkeyAction] = Field(
        None, description="Only trigger events for this action."
    )
    ignoreHotkeysTriggeredByAPI: bool = Field(
        False, description="Ignore hotkeys triggered by the API."
    )


class HotkeyTriggeredEventSubscriptionRequestData(BaseModel):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.HotkeyTriggeredEvent] = EventType.HotkeyTriggeredEvent
    subscribe: bool = True
    config: HotkeyTriggeredEventSubscriptionRequestConfig


class HotkeyTriggeredEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: HotkeyTriggeredEventSubscriptionRequestData


class HotkeyTriggeredEventData(BaseModel):
    """Data for model loaded event."""

    hotkeyID: str
    hotkeyName: str
    hotkeyAction: HotkeyAction
    hotkeyFile: str
    hotkeyTriggeredByAPI: bool
    modelID: str
    modelName: str
    isLive2DItem: bool


class HotkeyTriggeredEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.HotkeyTriggeredEvent] = EventType.HotkeyTriggeredEvent
    data: HotkeyTriggeredEventData


# ============================================================================
# Animation Events
# ============================================================================


class ModelAnimationEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""

    ignoreLive2DItems: bool = Field(False, description="Ignore live2d items.")
    ignoreIdleAnimations: bool = Field(False, description="Ignore idle animations.")


class ModelAnimationEventSubscriptionRequestData(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ModelAnimationEvent] = EventType.ModelAnimationEvent
    subscribe: bool = True
    config: ModelAnimationEventSubscriptionRequestConfig


class ModelAnimationEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: ModelAnimationEventSubscriptionRequestData


class ModelAnimationEventData(BaseModel):
    """Data for model loaded event."""

    animationEventType: AnimationEventType
    animationEventTime: float
    animationEventData: str
    animationName: str
    animationLength: float
    isIdleAnimation: bool
    modelID: str
    modelName: str
    isLive2DItem: bool


class ModelAnimationEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.ModelAnimationEvent] = EventType.ModelAnimationEvent
    data: ModelAnimationEventData


# ============================================================================
# Item Events
# ============================================================================


class ItemEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""

    itemInstanceIDs: Optional[List[str]] = Field(
        None, description="The IDs of the items to listen for."
    )
    itemFileNames: Optional[List[str]] = Field(
        None, description="The file names of the items to listen for."
    )


class ItemEventSubscriptionRequestData(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ItemEvent] = EventType.ItemEvent
    subscribe: bool = True
    config: ItemEventSubscriptionRequestConfig


class ItemEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: ItemEventSubscriptionRequestData


class ItemPosition(BaseModel):
    x: float
    y: float


class ItemEventData(BaseModel):
    """Data for model loaded event."""

    itemEventType: ItemEventType
    itemInstanceID: str
    itemFileName: str
    itemPosition: ItemPosition


class ItemEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.ItemEvent] = EventType.ItemEvent
    data: ItemEventData


# ============================================================================
# Model Clicked Events
# ============================================================================


class ModelClickedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""

    onlyClicksOnModel: Optional[bool] = Field(
        True, description="Only trigger events for clicks on the model."
    )


class ModelClickedEventSubscriptionRequestData(BaseModel):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ModelClickedEvent] = EventType.ModelClickedEvent
    subscribe: bool = True
    config: ModelClickedEventSubscriptionRequestConfig


class ModelClickedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: ModelClickedEventSubscriptionRequestData


class HitInfo(BaseModel):
    modelID: str
    artMeshID: str
    angle: float
    size: float
    vertexID1: int
    vertexID2: int
    vertexID3: int
    vertexWeight1: float
    vertexWeight2: float
    vertexWeight3: float


class ArtMeshHit(BaseModel):
    artMeshOrder: int
    isMasked: bool
    hitInfo: HitInfo


class ClickPosition(BaseModel):
    x: float
    y: float


class ModelClickedEventData(BaseModel):
    """Data for model loaded event."""

    modelLoaded: bool
    loadedModelID: str
    loadedModelName: str
    modelWasClicked: bool
    mouseButtonID: MouseButtonID
    clickPosition: ClickPosition
    windowSize: WindowSize
    clickedArtMeshCount: int
    artMeshHits: List[ArtMeshHit]


class ModelClickedEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.ModelClickedEvent] = EventType.ModelClickedEvent
    data: ModelClickedEventData


# ============================================================================
# Post Processing Events
# ============================================================================


class PostProcessingEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""


class PostProcessingEventSubscriptionRequestData(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.PostProcessingEvent] = EventType.PostProcessingEvent
    subscribe: bool = True
    config: PostProcessingEventSubscriptionRequestConfig


class PostProcessingEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: PostProcessingEventSubscriptionRequestData


class PostProcessingEventData(BaseModel):
    """Data for model loaded event."""

    currentState: bool
    currentPreset: str


class PostProcessingEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.PostProcessingEvent] = EventType.PostProcessingEvent
    data: PostProcessingEventData


# ============================================================================
# Live2D Cubism Editor  Events
# ============================================================================


class Live2DCubismEditorConnectedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""


class Live2DCubismEditorConnectedEventSubscriptionRequestData(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.Live2DCubismEditorConnectedEvent] = (
        EventType.Live2DCubismEditorConnectedEvent
    )
    subscribe: bool = True
    config: Live2DCubismEditorConnectedEventSubscriptionRequestConfig


class Live2DCubismEditorConnectedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    data: Live2DCubismEditorConnectedEventSubscriptionRequestData


class Live2DCubismEditorConnectedEventData(BaseModel):
    """Data for model loaded event."""

    tryingToConnect: bool
    connected: bool
    shouldSendParameters: bool


class Live2DCubismEditorConnectedEvent(BaseEvent):
    """Event fired when a model is loaded."""

    messageType: Literal[EventType.Live2DCubismEditorConnectedEvent] = (
        EventType.Live2DCubismEditorConnectedEvent
    )
    data: Live2DCubismEditorConnectedEventData


# Mapping of event types to their corresponding Pydantic models
EVENT_MODEL_MAP: Dict[EventType, type] = {
    EventType.TestEvent: TestEvent,
    EventType.ModelLoadedEvent: ModelLoadedEvent,
    EventType.TrackingStatusChangedEvent: TrackingStatusChangedEvent,
    EventType.BackgroundChangedEvent: BackgroundChangedEvent,
    EventType.ModelConfigChangedEvent: ModelConfigChangedEvent,
    EventType.ModelMovedEvent: ModelMovedEvent,
    EventType.ModelOutlineEvent: ModelOutlineEvent,
    EventType.HotkeyTriggeredEvent: HotkeyTriggeredEvent,
    EventType.ModelAnimationEvent: ModelAnimationEvent,
    EventType.ItemEvent: ItemEvent,
    EventType.ModelClickedEvent: ModelClickedEvent,
    EventType.PostProcessingEvent: PostProcessingEvent,
    EventType.Live2DCubismEditorConnectedEvent: Live2DCubismEditorConnectedEvent,
}
