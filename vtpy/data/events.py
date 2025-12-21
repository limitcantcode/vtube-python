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
    "WindowSize",
    "AnimationEventType",
    "ItemEventType",
    "BaseEventSubscriptionRequest",
    "EventSubscriptionResponseData",
    "EventSubscriptionResponse",
    "MouseButtonID",
    "TestEventSubscriptionRequestConfig",
    "TestEventSubscriptionRequest",
    "TestEventData",
    "TestEvent",
    "ModelLoadedEventSubscriptionRequestConfig",
    "ModelLoadedEventSubscriptionRequest",
    "ModelLoadedEventData",
    "ModelLoadedEvent",
    "TrackingStatusChangedEventSubscriptionRequestConfig",
    "TrackingStatusChangedEventSubscriptionRequest",
    "TrackingStatusChangedEventData",
    "TrackingStatusChangedEvent",
    "BackgroundChangedEventSubscriptionRequestConfig",
    "BackgroundChangedEventSubscriptionRequest",
    "BackgroundChangedEventData",
    "BackgroundChangedEvent",
    "ModelConfigModifiedEventSubscriptionRequestConfig",
    "ModelConfigModifiedEventSubscriptionRequest",
    "ModelConfigModifiedEventData",
    "ModelConfigModifiedEvent",
    "ModelMovedEventSubscriptionRequestConfig",
    "ModelMovedEventSubscriptionRequest",
    "ModelPositionData",
    "ModelMovedEventData",
    "ModelMovedEvent",
    "ModelOutlineEventSubscriptionRequestConfig",
    "ModelOutlineEventSubscriptionRequest",
    "ConvexHullPoint",
    "ModelOutlineEventData",
    "ModelOutlineEvent",
    "HotkeyTriggeredEventSubscriptionRequestConfig",
    "HotkeyTriggeredEventSubscriptionRequest",
    "HotkeyTriggeredEventData",
    "HotkeyTriggeredEvent",
    "ModelAnimationEventSubscriptionRequestConfig",
    "ModelAnimationEventSubscriptionRequest",
    "ModelAnimationEventData",
    "ModelAnimationEvent",
    "ItemEventSubscriptionRequestConfig",
    "ItemEventSubscriptionRequest",
    "ItemPosition",
    "ItemEventData",
    "ItemEvent",
    "ModelClickedEventSubscriptionRequestConfig",
    "ModelClickedEventSubscriptionRequest",
    "HitInfo",
    "ArtMeshHit",
    "ClickPosition",
    "ModelClickedEventData",
    "ModelClickedEvent",
    "PostProcessingEventSubscriptionRequestConfig",
    "PostProcessingEventSubscriptionRequest",
    "PostProcessingEventData",
    "PostProcessingEvent",
    "Live2DCubismEditorConnectedEventSubscriptionRequestConfig",
    "Live2DCubismEditorConnectedEventSubscriptionRequest",
    "Live2DCubismEditorConnectedEventData",
    "Live2DCubismEditorConnectedEvent",
]
# ============================================================================
# Helper Types
# ============================================================================


class WindowSize(BaseModel):
    x: float
    y: float


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

    testMessageForEvent: str = Field(description="Test message returned in the event.")


class TestEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.TestEvent] = EventType.TestEvent
    config: TestEventSubscriptionRequestConfig


class TestEventData(BaseModel):
    """Data for model loaded event."""

    yourTestMessage: str = Field(description="Test message returned in the event.")
    counter: int = Field(description="Counter of the event.")


class TestEvent(BaseEvent):
    """Event fired when a model is loaded."""

    eventName: Literal[EventType.TestEvent] = EventType.TestEvent
    data: TestEventData


# ============================================================================
# Model Events
# ============================================================================


class ModelLoadedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""

    modelID: Optional[List[str]] = Field(None, description="The ID of the model to listen for.")


class ModelLoadedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ModelLoadedEvent] = EventType.ModelLoadedEvent
    config: ModelLoadedEventSubscriptionRequestConfig


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


class TrackingStatusChangedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.TrackingStatusChangedEvent] = EventType.TrackingStatusChangedEvent
    config: TrackingStatusChangedEventSubscriptionRequestConfig


class TrackingStatusChangedEventData(BaseModel):
    """Data for model loaded event."""

    faceFound: bool
    leftHandFound: bool
    rightHandFound: bool


class TrackingStatusChangedEvent(BaseEvent):
    """Event fired when a model is loaded."""

    eventName: Literal[EventType.TrackingStatusChangedEvent] = EventType.TrackingStatusChangedEvent
    data: TrackingStatusChangedEventData


# ============================================================================
# Background Events
# ============================================================================


class BackgroundChangedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""


class BackgroundChangedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.BackgroundChangedEvent] = EventType.BackgroundChangedEvent
    config: BackgroundChangedEventSubscriptionRequestConfig


class BackgroundChangedEventData(BaseModel):
    """Data for model loaded event."""

    backgroundName: str


class BackgroundChangedEvent(BaseEvent):
    """Event fired when a model is loaded."""

    eventName: Literal[EventType.BackgroundChangedEvent] = EventType.BackgroundChangedEvent
    data: BackgroundChangedEventData


# ============================================================================
# Model Config Events
# ============================================================================


class ModelConfigModifiedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""


class ModelConfigModifiedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ModelConfigModifiedEvent] = EventType.ModelConfigModifiedEvent
    config: ModelConfigModifiedEventSubscriptionRequestConfig


class ModelConfigModifiedEventData(BaseModel):
    """Data for model loaded event."""

    modelID: str
    modelName: str
    hotkeyConfigChanged: bool


class ModelConfigModifiedEvent(BaseEvent):
    """Event fired when a model is loaded."""

    eventName: Literal[EventType.ModelConfigModifiedEvent] = EventType.ModelConfigModifiedEvent
    data: ModelConfigModifiedEventData


# ============================================================================
# Model Moved Events
# ============================================================================


class ModelMovedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""


class ModelMovedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ModelMovedEvent] = EventType.ModelMovedEvent
    config: ModelMovedEventSubscriptionRequestConfig


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

    eventName: Literal[EventType.ModelMovedEvent] = EventType.ModelMovedEvent
    data: ModelMovedEventData


# ============================================================================
# Model Outline Events
# ============================================================================


class ModelOutlineEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""

    draw: bool


class ModelOutlineEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ModelOutlineEvent] = EventType.ModelOutlineEvent
    config: ModelOutlineEventSubscriptionRequestConfig


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

    eventName: Literal[EventType.ModelOutlineEvent] = EventType.ModelOutlineEvent
    data: ModelOutlineEventData


# ============================================================================
# Hotkey Events
# ============================================================================


class HotkeyTriggeredEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""

    onlyForAction: HotkeyAction
    ignoreHotkeysTriggeredByAPI: bool


class HotkeyTriggeredEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.HotkeyTriggeredEvent] = EventType.HotkeyTriggeredEvent
    config: HotkeyTriggeredEventSubscriptionRequestConfig


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

    eventName: Literal[EventType.HotkeyTriggeredEvent] = EventType.HotkeyTriggeredEvent
    data: HotkeyTriggeredEventData


# ============================================================================
# Animation Events
# ============================================================================


class ModelAnimationEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""

    ignoreLive2DItems: bool
    ignoreIdleAnimations: bool


class ModelAnimationEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ModelAnimationEvent] = EventType.ModelAnimationEvent
    config: ModelAnimationEventSubscriptionRequestConfig


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

    eventName: Literal[EventType.ModelAnimationEvent] = EventType.ModelAnimationEvent
    data: ModelAnimationEventData


# ============================================================================
# Item Events
# ============================================================================


class ItemEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""

    itemInstanceIDs: List[str]
    itemFileNames: List[str]


class ItemEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ItemEvent] = EventType.ItemEvent
    config: ItemEventSubscriptionRequestConfig


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

    eventName: Literal[EventType.ItemEvent] = EventType.ItemEvent
    data: ItemEventData


# ============================================================================
# Model Clicked Events
# ============================================================================


class ModelClickedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""

    onlyClicksOnModel: bool


class ModelClickedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.ModelClickedEvent] = EventType.ModelClickedEvent
    config: ModelClickedEventSubscriptionRequestConfig


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

    eventName: Literal[EventType.ModelClickedEvent] = EventType.ModelClickedEvent
    data: ModelClickedEventData


# ============================================================================
# Post Processing Events
# ============================================================================


class PostProcessingEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""


class PostProcessingEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.PostProcessingEvent] = EventType.PostProcessingEvent
    config: PostProcessingEventSubscriptionRequestConfig


class PostProcessingEventData(BaseModel):
    """Data for model loaded event."""

    currentState: bool
    currentPreset: str


class PostProcessingEvent(BaseEvent):
    """Event fired when a model is loaded."""

    eventName: Literal[EventType.PostProcessingEvent] = EventType.PostProcessingEvent
    data: PostProcessingEventData


# ============================================================================
# Live2D Cubism Editor  Events
# ============================================================================


class Live2DCubismEditorConnectedEventSubscriptionRequestConfig(BaseModel):
    """Config for model loaded event subscription request."""


class Live2DCubismEditorConnectedEventSubscriptionRequest(BaseEventSubscriptionRequest):
    """Request to subscribe to model loaded events."""

    eventName: Literal[EventType.Live2DCubismEditorConnectedEvent] = (
        EventType.Live2DCubismEditorConnectedEvent
    )
    config: Live2DCubismEditorConnectedEventSubscriptionRequestConfig


class Live2DCubismEditorConnectedEventData(BaseModel):
    """Data for model loaded event."""

    tryingToConnect: bool
    connected: bool
    shouldSendParameters: bool


class Live2DCubismEditorConnectedEvent(BaseEvent):
    """Event fired when a model is loaded."""

    eventName: Literal[EventType.Live2DCubismEditorConnectedEvent] = (
        EventType.Live2DCubismEditorConnectedEvent
    )
    data: Live2DCubismEditorConnectedEventData
