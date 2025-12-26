"""Request and response data models for VTube Studio API."""

from ast import For
from typing import Optional, List, Dict, Any, Literal, Union
from enum import Enum
from pydantic import BaseModel, Field
from vtpy.data.common import BaseRequest, BaseResponse, ErrorData, MessageType, HotkeyAction
from vtpy.data.effects import PostProcessingEffect, PostProcessingEffectConfigID


__all__ = [
    "ItemType",
    "PermissionType",
    "ParameterMode",
    "FadeMode",
    "ItemSplitPoint",
    "ItemSortOrder",
    "WithinModelOrder",
    "AngleRelativeTo",
    "SizeRelativeTo",
    "VertexPinType",
    "Parameter",
    "ItemInstance",
    "ItemFile",
    "PermissionRequestData",
    "PermissionRequest",
    "PermissionGrantedResult",
    "PermissionResponseData",
    "PermissionResponse",
    "AuthenticationRequestData",
    "AuthenticationRequest",
    "AuthenticationResponseData",
    "AuthenticationResponse",
    "AuthenticationTokenRequestData",
    "AuthenticationTokenRequest",
    "AuthenticationTokenResponseData",
    "AuthenticationTokenResponse",
    "StatisticsRequestData",
    "StatisticsRequest",
    "StatisticsResponseData",
    "StatisticsResponse",
    "VTSFolderInfoRequestData",
    "VTSFolderInfoRequest",
    "VTSFolderInfoResponseData",
    "VTSFolderInfoResponse",
    "CurrentModelRequestData",
    "CurrentModelRequest",
    "ModelPosition",
    "CurrentModelResponseData",
    "CurrentModelResponse",
    "AvailableModelsRequestData",
    "AvailableModelsRequest",
    "AvailableModel",
    "AvailableModelsResponseData",
    "AvailableModelsResponse",
    "ModelLoadRequestData",
    "ModelLoadRequest",
    "ModelLoadResponseData",
    "ModelLoadResponse",
    "MoveModelRequestData",
    "MoveModelRequest",
    "MoveModelResponseData",
    "MoveModelResponse",
    "HotkeysInCurrentModelRequestData",
    "HotkeysInCurrentModelRequest",
    "AvailableHotkey",
    "HotkeysInCurrentModelResponseData",
    "HotkeysInCurrentModelResponse",
    "HotkeyTriggerRequestData",
    "HotkeyTriggerRequest",
    "HotkeyTriggerResponseData",
    "HotkeyTriggerResponse",
    "ExpressionStateRequestData",
    "ExpressionStateRequest",
    "Hotkey",
    "Expression",
    "ExpressionStateResponseData",
    "ExpressionStateResponse",
    "ExpressionActivationRequestData",
    "ExpressionActivationRequest",
    "ExpressionActivationResponseData",
    "ExpressionActivationResponse",
    "ArtMeshListRequestData",
    "ArtMeshListRequest",
    "ArtMeshListResponseData",
    "ArtMeshListResponse",
    "ColorTintData",
    "ArtMeshMatcherData",
    "ColorTintRequestData",
    "ColorTintRequest",
    "ColorTintResponseData",
    "ColorTintResponse",
    "SceneColorOverlayInfoRequestData",
    "SceneColorOverlayInfoRequest",
    "LeftCapturePart",
    "MiddleCapturePart",
    "RightCapturePart",
    "SceneColorOverlayInfoResponseData",
    "SceneColorOverlayInfoResponse",
    "FaceFoundRequestData",
    "FaceFoundRequest",
    "FaceFoundResponseData",
    "FaceFoundResponse",
    "InputParameterListRequestData",
    "InputParameterListRequest",
    "InputParameterListResponseData",
    "InputParameterListResponse",
    "ParameterValueRequestData",
    "ParameterValueRequest",
    "ParameterValueResponseData",
    "ParameterValueResponse",
    "Live2DParameterListRequestData",
    "Live2DParameterListRequest",
    "Live2DParameterListResponseData",
    "Live2DParameterListResponse",
    "ParameterCreationRequestData",
    "ParameterCreationRequest",
    "ParameterCreationResponseData",
    "ParameterCreationResponse",
    "ParameterDeletionRequestData",
    "ParameterDeletionRequest",
    "ParameterDeletionResponseData",
    "ParameterDeletionResponse",
    "ParameterValue",
    "InjectParameterDataRequestData",
    "InjectParameterDataRequest",
    "InjectParameterDataResponseData",
    "InjectParameterDataResponse",
    "GetCurrentModelPhysicsRequestData",
    "GetCurrentModelPhysicsRequest",
    "PhysicsGroup",
    "GetCurrentModelPhysicsResponseData",
    "GetCurrentModelPhysicsResponse",
    "StrengthOverride",
    "WindOverride",
    "SetCurrentModelPhysicsRequestData",
    "SetCurrentModelPhysicsRequest",
    "SetCurrentModelPhysicsResponseData",
    "SetCurrentModelPhysicsResponse",
    "NDIConfigRequestData",
    "NDIConfigRequest",
    "NDIConfigResponseData",
    "NDIConfigResponse",
    "ItemListRequestData",
    "ItemListRequest",
    "ItemListResponseData",
    "ItemListResponse",
    "ItemLoadRequestData",
    "ItemLoadRequest",
    "ItemLoadResponseData",
    "ItemLoadResponse",
    "ItemUnloadRequestData",
    "ItemUnloadRequest",
    "ItemUnloadedItem",
    "ItemUnloadResponseData",
    "ItemUnloadResponse",
    "ItemAnimationControlRequestData",
    "ItemAnimationControlRequest",
    "ItemAnimationControlResponseData",
    "ItemAnimationControlResponse",
    "ItemMoveRequestItem",
    "ItemMoveRequestData",
    "ItemMoveRequest",
    "MovedItem",
    "ItemMoveResponseData",
    "ItemMoveResponse",
    "ItemSortRequestData",
    "ItemSortRequest",
    "ItemSortResponseData",
    "ItemSortResponse",
    "ArtMeshSelectionRequestData",
    "ArtMeshSelectionRequest",
    "ArtMeshSelectionResponseData",
    "ArtMeshSelectionResponse",
    "PinInfo",
    "ItemPinRequestData",
    "ItemPinRequest",
    "ItemPinResponseData",
    "ItemPinResponse",
    "PostProcessingListRequestData",
    "PostProcessingListRequest",
    "PostProcessingEffectConfigInfo",
    "PostProcessingEffectInfo",
    "PostProcessingListResponseData",
    "PostProcessingListResponse",
    "PostProcessingUpdateValue",
    "PostProcessingUpdateRequestData",
    "PostProcessingUpdateRequest",
    "PostProcessingUpdateResponseData",
    "PostProcessingUpdateResponse",
]


class Parameter(BaseModel):
    name: str
    addedBy: str
    value: float
    min: float
    max: float
    defaultValue: float


class ItemType(Enum):
    PNG = "PNG"
    JPEG = "JPEG"
    GIF = "GIF"
    LIVE2D = "Live2D"
    AnimationFolder = "AnimationFolder"
    Unknown = "Unknown"


class ItemInstance(BaseModel):
    fileName: str
    instanceID: str
    order: int
    type: ItemType
    censored: bool
    flipped: bool
    locked: bool
    smoothing: float
    framerate: float
    frameCount: int
    currentFrame: int
    pinnedToModel: bool
    pinnedModelID: str
    pinnedArtMeshID: str
    groupName: str
    sceneName: str
    fromWorkshop: bool


class ItemFile(BaseModel):
    fileName: str
    type: ItemType
    loadedCount: int


# ============================================================================
# API Permissions
# ============================================================================


class PermissionType(Enum):
    """Type of permission requested."""

    LoadCustomImagesAsItems = "LoadCustomImagesAsItems"


class PermissionRequestData(BaseModel):
    """Data for authentication request."""

    requestedPermission: PermissionType = Field(description="The permission type.")


class PermissionRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.PermissionRequest] = MessageType.PermissionRequest
    data: PermissionRequestData


class PermissionGrantedResult(BaseModel):
    name: PermissionType
    granted: bool


class PermissionResponseData(BaseModel):
    """Data for authentication response."""

    grantSuccess: bool
    requestedPermission: PermissionType
    permissions: List[PermissionGrantedResult]


class PermissionResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.PermissionResponse] = MessageType.PermissionResponse
    data: Union[PermissionResponseData, ErrorData]


# ============================================================================
# Authentication Using Token
# ============================================================================


class AuthenticationRequestData(BaseModel):
    """Data for authentication request."""

    pluginName: str = Field(description="The name of the plugin.")
    pluginDeveloper: str = Field(description="The developer of the plugin.")
    authenticationToken: str = Field(description="The authentication token.")


class AuthenticationRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.AuthenticationRequest] = MessageType.AuthenticationRequest
    data: AuthenticationRequestData


class AuthenticationResponseData(BaseModel):
    """Data for authentication response."""

    authenticated: bool
    reason: Optional[str] = None


class AuthenticationResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.AuthenticationResponse] = MessageType.AuthenticationResponse
    data: Union[AuthenticationResponseData, ErrorData]


# ============================================================================
# Authentication Get Token
# ============================================================================


class AuthenticationTokenRequestData(BaseModel):
    """Data for authentication request."""

    pluginName: str = Field(description="The name of the plugin.")
    pluginDeveloper: str = Field(description="The developer of the plugin.")
    pluginIcon: Optional[str] = Field(None, description="The icon of the plugin.")


class AuthenticationTokenRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.AuthenticationTokenRequest] = (
        MessageType.AuthenticationTokenRequest
    )
    data: AuthenticationTokenRequestData


class AuthenticationTokenResponseData(BaseModel):
    """Data for authentication response."""

    authenticationToken: str


class AuthenticationTokenResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.AuthenticationTokenResponse] = (
        MessageType.AuthenticationTokenResponse
    )
    data: Union[AuthenticationTokenResponseData, ErrorData]


# ============================================================================
# VTS Stats
# ============================================================================


class StatisticsRequestData(BaseModel):
    """Data for authentication request."""


class StatisticsRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.StatisticsRequest] = MessageType.StatisticsRequest
    data: StatisticsRequestData


class StatisticsResponseData(BaseModel):
    """Data for authentication response."""

    uptime: int
    framerate: int
    vTubeStudioVersion: str
    allowedPlugins: int
    connectedPlugins: int
    startedWithSteam: bool
    windowWidth: int
    windowHeight: int
    windowIsFullscreen: bool


class StatisticsResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.StatisticsResponse] = MessageType.StatisticsResponse
    data: Union[StatisticsResponseData, ErrorData]


# ============================================================================
# VTS Folders
# ============================================================================


class VTSFolderInfoRequestData(BaseModel):
    """Data for authentication request."""


class VTSFolderInfoRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.VTSFolderInfoRequest] = MessageType.VTSFolderInfoRequest
    data: VTSFolderInfoRequestData


class VTSFolderInfoResponseData(BaseModel):
    """Data for authentication response."""

    models: str
    backgrounds: str
    items: str
    config: str
    logs: str
    backup: str


class VTSFolderInfoResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.VTSFolderInfoResponse] = MessageType.VTSFolderInfoResponse
    data: Union[VTSFolderInfoResponseData, ErrorData]


# ============================================================================
# Get Loaded Model
# ============================================================================


class CurrentModelRequestData(BaseModel):
    """Data for authentication request."""


class CurrentModelRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.CurrentModelRequest] = MessageType.CurrentModelRequest
    data: CurrentModelRequestData


class ModelPosition(BaseModel):
    positionX: float
    positionY: float
    rotation: float
    size: float


class CurrentModelResponseData(BaseModel):
    """Data for authentication response."""

    modelLoaded: bool
    modelName: str
    modelID: str
    vtsModelName: str
    vtsModelIconName: str
    live2DModelName: str
    modelLoadTime: int
    timeSinceModelLoaded: int
    numberOfLive2DParameters: int
    numberOfLive2DArtmeshes: int
    hasPhysicsFile: bool
    numberOfTextures: int
    textureResolution: int
    modelPosition: ModelPosition


class CurrentModelResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.CurrentModelResponse] = MessageType.CurrentModelResponse
    data: Union[CurrentModelResponseData, ErrorData]


# ============================================================================
# Get Model List
# ============================================================================


class AvailableModelsRequestData(BaseModel):
    """Data for authentication request."""


class AvailableModelsRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.AvailableModelsRequest] = MessageType.AvailableModelsRequest
    data: AvailableModelsRequestData


class AvailableModel(BaseModel):
    modelLoaded: bool
    modelName: str
    modelID: str
    vtsModelName: str
    vtsModelIconName: str


class AvailableModelsResponseData(BaseModel):
    """Data for authentication response."""

    numberOfModels: int
    availableModels: List[AvailableModel]


class AvailableModelsResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.AvailableModelsResponse] = MessageType.AvailableModelsResponse
    data: Union[AvailableModelsResponseData, ErrorData]


# ============================================================================
# Load Model
# ============================================================================


class ModelLoadRequestData(BaseModel):
    """Data for authentication request."""

    modelID: Optional[str] = Field(None, description="The ID of the model to load.")


class ModelLoadRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ModelLoadRequest] = MessageType.ModelLoadRequest
    data: ModelLoadRequestData


class ModelLoadResponseData(BaseModel):
    """Data for authentication response."""

    modelID: Optional[str] = Field(None, description="The ID of the model that was loaded.")


class ModelLoadResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ModelLoadResponse] = MessageType.ModelLoadResponse
    data: Union[ModelLoadResponseData, ErrorData]


# ============================================================================
# Move Model
# ============================================================================


class MoveModelRequestData(BaseModel):
    """Data for authentication request."""

    timeInSeconds: float = Field(
        1, description="The time in seconds to move the model.", ge=0, le=2
    )
    valuesAreRelativeToModel: bool = Field(
        True, description="Whether the values are relative to the model's current position."
    )
    positionX: Optional[float] = Field(
        None, description="The X position of the model.", ge=-1000, le=1000
    )
    positionY: Optional[float] = Field(
        None, description="The Y position of the model.", ge=-1000, le=1000
    )
    rotation: Optional[float] = Field(
        None, description="The rotation of the model.", ge=-360, le=360
    )
    size: Optional[float] = Field(None, description="The size of the model.", ge=-100, le=100)


class MoveModelRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.MoveModelRequest] = MessageType.MoveModelRequest
    data: MoveModelRequestData


class MoveModelResponseData(BaseModel):
    """Data for authentication response."""


class MoveModelResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.MoveModelResponse] = MessageType.MoveModelResponse
    data: Union[MoveModelResponseData, ErrorData]


# ============================================================================
# Hotkeys Get List
# ============================================================================


class HotkeysInCurrentModelRequestData(BaseModel):
    """Data for authentication request."""

    modelID: Optional[str] = Field(
        None, description="The ID of the model to get hotkeys for if not the current model."
    )
    live2DItemFileName: Optional[str] = Field(
        None, description="The file name of the live2d item to get hotkeys for."
    )


class HotkeysInCurrentModelRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.HotkeysInCurrentModelRequest] = (
        MessageType.HotkeysInCurrentModelRequest
    )
    data: HotkeysInCurrentModelRequestData


class AvailableHotkey(BaseModel):
    name: str
    type: HotkeyAction
    description: str
    file: str
    hotkeyID: str
    keyCombination: List[str]  # TODO: confirm this is actually strings and not ints
    onScreenButtonID: int


class HotkeysInCurrentModelResponseData(BaseModel):
    """Data for authentication response."""

    modelLoaded: bool
    modelName: str
    modelID: str
    availableHotkeys: List[AvailableHotkey]


class HotkeysInCurrentModelResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.HotkeysInCurrentModelResponse] = (
        MessageType.HotkeysInCurrentModelResponse
    )
    data: Union[HotkeysInCurrentModelResponseData, ErrorData]


# ============================================================================
# Hotkeys Trigger
# ============================================================================


class HotkeyTriggerRequestData(BaseModel):
    """Data for authentication request."""

    hotkeyID: str = Field(description="The ID of the hotkey to trigger.")
    itemInstanceID: Optional[str] = Field(
        None, description="The instance ID of the optional item to trigger the hotkey for."
    )


class HotkeyTriggerRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.HotkeyTriggerRequest] = MessageType.HotkeyTriggerRequest
    data: HotkeyTriggerRequestData


class HotkeyTriggerResponseData(BaseModel):
    """Data for authentication response."""

    hotkeyID: str


class HotkeyTriggerResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.HotkeyTriggerResponse] = MessageType.HotkeyTriggerResponse
    data: Union[HotkeyTriggerResponseData, ErrorData]


# ============================================================================
# Expression Get List
# ============================================================================


class ExpressionStateRequestData(BaseModel):
    """Data for authentication request."""

    details: bool = Field(
        True, description="Whether to return detailed information about the expression."
    )
    expressionFile: Optional[str] = Field(
        None, description="The file name of the expression to get the state of."
    )


class ExpressionStateRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ExpressionStateRequest] = MessageType.ExpressionStateRequest
    data: ExpressionStateRequestData


class Hotkey(BaseModel):
    name: str
    id: str


class Parameter(BaseModel):
    name: str
    value: float


class Expression(BaseModel):
    name: str
    file: str
    active: bool
    deactivateWhenKeyIsLetGo: bool
    autoDeactivateAfterSeconds: bool
    secondsRemaining: float
    usedInHotkeys: List[Hotkey]
    parameters: List[Parameter]


class ExpressionStateResponseData(BaseModel):
    """Data for authentication response."""

    modelLoaded: bool
    modelName: str
    modelID: str
    expressions: List[Expression]


class ExpressionStateResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ExpressionStateResponse] = MessageType.ExpressionStateResponse
    data: Union[ExpressionStateResponseData, ErrorData]


# ============================================================================
# Expression Toggle
# ============================================================================


class ExpressionActivationRequestData(BaseModel):
    """Data for authentication request."""

    expressionFile: str = Field(description="The file name of the expression to activate.")
    fadeTime: float = Field(
        0.25, description="The time in seconds to fade in the expression.", ge=0, le=2
    )
    active: bool = Field(True, description="Whether to activate the expression.")


class ExpressionActivationRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ExpressionActivationRequest] = (
        MessageType.ExpressionActivationRequest
    )
    data: ExpressionActivationRequestData


class ExpressionActivationResponseData(BaseModel):
    """Data for authentication response."""


class ExpressionActivationResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ExpressionActivationResponse] = (
        MessageType.ExpressionActivationResponse
    )
    data: Union[ExpressionActivationResponseData, ErrorData]


# ============================================================================
# Artmesh Get List
# ============================================================================


class ArtMeshListRequestData(BaseModel):
    """Data for authentication request."""


class ArtMeshListRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ArtMeshListRequest] = MessageType.ArtMeshListRequest
    data: ArtMeshListRequestData


class ArtMeshListResponseData(BaseModel):
    """Data for authentication response."""

    modelLoaded: bool
    numberOfArtMeshNames: int
    numberOfArtMeshTags: int
    artMeshNames: List[str]
    artMeshTags: List[str]


class ArtMeshListResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ArtMeshListResponse] = MessageType.ArtMeshListResponse
    data: Union[ArtMeshListResponseData, ErrorData]


# ============================================================================
# Artmesh Color Tint
# ============================================================================


class ColorTintData(BaseModel):
    colorR: int = Field(description="The red color value.")
    colorG: int = Field(description="The green color value.")
    colorB: int = Field(description="The blue color value.")
    colorA: int = Field(description="The alpha color value.")
    mixWithSceneLightingColor: Optional[float] = Field(
        1, description="The amount to mix with the scene lighting color.", ge=0, le=1
    )


class ArtMeshMatcherData(BaseModel):
    tintAll: bool = Field(True, description="Whether to tint all art meshes.")
    artMeshNumber: Optional[List[int]] = Field(
        None, description="The numbers of the art meshes to tint."
    )
    nameExact: Optional[List[str]] = Field(
        None, description="The exact names of the art meshes to tint."
    )
    nameContains: Optional[List[str]] = Field(
        None, description="The names of the art meshes to tint."
    )
    tagExact: Optional[List[str]] = Field(
        None, description="The exact tags of the art meshes to tint."
    )
    tagContains: Optional[List[str]] = Field(
        None, description="The tags of the art meshes to tint."
    )


class ColorTintRequestData(BaseModel):
    """Data for authentication request."""

    colorTint: ColorTintData = Field(description="The color tint data.")
    artMeshMatcher: ArtMeshMatcherData = Field(description="The art mesh matcher data.")


class ColorTintRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ColorTintRequest] = MessageType.ColorTintRequest
    data: ColorTintRequestData


class ColorTintResponseData(BaseModel):
    """Data for authentication response."""

    matchedArtMeshes: int


class ColorTintResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ColorTintResponse] = MessageType.ColorTintResponse
    data: Union[ColorTintResponseData, ErrorData]


# ============================================================================
# Scene Color Overlay Info
# ============================================================================


class SceneColorOverlayInfoRequestData(BaseModel):
    """Data for authentication request."""


class SceneColorOverlayInfoRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.SceneColorOverlayInfoRequest] = (
        MessageType.SceneColorOverlayInfoRequest
    )
    data: SceneColorOverlayInfoRequestData


class LeftCapturePart(BaseModel):
    active: bool
    colorR: int
    colorG: int
    colorB: int


class MiddleCapturePart(BaseModel):
    active: bool
    colorR: int
    colorG: int
    colorB: int


class RightCapturePart(BaseModel):
    active: bool
    colorR: int
    colorG: int
    colorB: int


class SceneColorOverlayInfoResponseData(BaseModel):
    """Data for authentication response."""

    active: bool
    itemsIncluded: bool
    isWindowCapture: bool
    baseBrightness: int
    colorBoost: int
    smoothing: int
    colorOverlayR: int
    colorOverlayG: int
    colorOverlayB: int
    colorAvgR: int
    colorAvgG: int
    colorAvgB: int
    leftCapturePart: LeftCapturePart
    middleCapturePart: MiddleCapturePart
    rightCapturePart: RightCapturePart


class SceneColorOverlayInfoResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.SceneColorOverlayInfoResponse] = (
        MessageType.SceneColorOverlayInfoResponse
    )
    data: Union[SceneColorOverlayInfoResponseData, ErrorData]


# ============================================================================
# Face Found
# ============================================================================


class FaceFoundRequestData(BaseModel):
    """Data for authentication request."""


class FaceFoundRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.FaceFoundRequest] = MessageType.FaceFoundRequest
    data: FaceFoundRequestData


class FaceFoundResponseData(BaseModel):
    """Data for authentication response."""

    found: bool


class FaceFoundResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.FaceFoundResponse] = MessageType.FaceFoundResponse
    data: Union[FaceFoundResponseData, ErrorData]


# ============================================================================
# Tracking Parameters Get List
# ============================================================================


class InputParameterListRequestData(BaseModel):
    """Data for authentication request."""


class InputParameterListRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.InputParameterListRequest] = (
        MessageType.InputParameterListRequest
    )
    data: InputParameterListRequestData


class InputParameterListResponseData(BaseModel):
    """Data for authentication response."""

    modelLoaded: bool
    modelName: str
    modelID: str
    customParameters: List[Parameter]
    defaultParameters: List[Parameter]


class InputParameterListResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.InputParameterListResponse] = (
        MessageType.InputParameterListResponse
    )
    data: Union[InputParameterListResponseData, ErrorData]


# ============================================================================
# Parameter Value Get
# ============================================================================


class ParameterValueRequestData(BaseModel):
    """Data for authentication request."""

    name: str = Field(description="The name of the parameter to get the value of.")


class ParameterValueRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ParameterValueRequest] = MessageType.ParameterValueRequest
    data: ParameterValueRequestData


class ParameterValueResponseData(Parameter):
    """Data for authentication response."""


class ParameterValueResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ParameterValueResponse] = MessageType.ParameterValueResponse
    data: Union[ParameterValueResponseData, ErrorData]


# ============================================================================
# Parameter Get All
# ============================================================================


class Live2DParameterListRequestData(BaseModel):
    """Data for authentication request."""


class Live2DParameterListRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.Live2DParameterListRequest] = (
        MessageType.Live2DParameterListRequest
    )
    data: Live2DParameterListRequestData


class Live2DParameterListResponseData(BaseModel):
    """Data for authentication response."""

    modelLoaded: bool
    modelName: str
    modelID: str
    parameters: List[Parameter]


class Live2DParameterListResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.Live2DParameterListResponse] = (
        MessageType.Live2DParameterListResponse
    )
    data: Union[Live2DParameterListResponseData, ErrorData]


# ============================================================================
# Parameter Add
# ============================================================================


class ParameterCreationRequestData(BaseModel):
    """Data for authentication request."""

    parameterName: str = Field(description="The name of the parameter to create.")
    explanation: Optional[str] = Field(
        None, description="The explanation of the parameter.", max_length=256
    )
    min: float = Field(
        -100, description="The minimum value of the parameter.", ge=-1000000, le=1000000
    )
    max: float = Field(
        100, description="The maximum value of the parameter.", ge=-1000000, le=1000000
    )
    defaultValue: float = Field(
        0, description="The default value of the parameter.", ge=-1000000, le=1000000
    )


class ParameterCreationRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ParameterCreationRequest] = (
        MessageType.ParameterCreationRequest
    )
    data: ParameterCreationRequestData


class ParameterCreationResponseData(BaseModel):
    """Data for authentication response."""

    parameterName: str


class ParameterCreationResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ParameterCreationResponse] = (
        MessageType.ParameterCreationResponse
    )
    data: Union[ParameterCreationResponseData, ErrorData]


# ============================================================================
# Parameter Delete
# ============================================================================


class ParameterDeletionRequestData(BaseModel):
    """Data for authentication request."""

    parameterName: str = Field(description="The name of the parameter to delete.")


class ParameterDeletionRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ParameterDeletionRequest] = (
        MessageType.ParameterDeletionRequest
    )
    data: ParameterDeletionRequestData


class ParameterDeletionResponseData(BaseModel):
    """Data for authentication response."""

    parameterName: str


class ParameterDeletionResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ParameterDeletionResponse] = (
        MessageType.ParameterDeletionResponse
    )
    data: Union[ParameterDeletionResponseData, ErrorData]


# ============================================================================
# Parameter Set
# ============================================================================


class ParameterMode(Enum):
    SET = "set"
    ADD = "add"


class ParameterValue(BaseModel):
    id: str = Field(description="The ID of the parameter to inject.")
    value: float = Field(
        description="The value of the parameter to inject.", ge=-1000000, le=1000000
    )
    weight: Optional[float] = Field(
        None, description="The weight of the parameter to inject.", ge=0, le=1
    )


class InjectParameterDataRequestData(BaseModel):
    """Data for authentication request."""

    faceFound: bool = Field(False, description="Signal face is found.")
    mode: ParameterMode = Field(
        ParameterMode.SET, description="The mode to inject the parameter in."
    )
    parameterValues: List[ParameterValue] = Field([], description="The parameters to inject.")


class InjectParameterDataRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.InjectParameterDataRequest] = (
        MessageType.InjectParameterDataRequest
    )
    data: InjectParameterDataRequestData


class InjectParameterDataResponseData(BaseModel):
    """Data for authentication response."""


class InjectParameterDataResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.InjectParameterDataResponse] = (
        MessageType.InjectParameterDataResponse
    )
    data: Union[InjectParameterDataResponseData, ErrorData]


# ============================================================================
# Physics Get
# ============================================================================


class GetCurrentModelPhysicsRequestData(BaseModel):
    """Data for authentication request."""


class GetCurrentModelPhysicsRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.GetCurrentModelPhysicsRequest] = (
        MessageType.GetCurrentModelPhysicsRequest
    )
    data: GetCurrentModelPhysicsRequestData


class PhysicsGroup(BaseModel):
    groupID: str
    groupName: str
    strengthMultiplier: float
    windMultiplier: float


class GetCurrentModelPhysicsResponseData(BaseModel):
    """Data for authentication response."""

    modelLoaded: bool
    modelName: str
    modelID: str
    modelHasPhysics: bool
    physicsSwitchedOn: bool
    usingLegacyPhysics: bool
    physicsFPSSetting: int
    baseStrength: int
    baseWind: int
    apiPhysicsOverrideActive: bool
    apiPhysicsOverridePluginName: str
    physicsGroups: List[PhysicsGroup]


class GetCurrentModelPhysicsResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.GetCurrentModelPhysicsResponse] = (
        MessageType.GetCurrentModelPhysicsResponse
    )
    data: Union[GetCurrentModelPhysicsResponseData, ErrorData]


# ============================================================================
# Physics Set
# ============================================================================


class StrengthOverride(BaseModel):
    id: str = Field(description="The ID of the parameter to override the strength of.")
    value: float = Field(description="The value of the strength override.", ge=0, le=100)
    setBaseValue: bool = Field(description="Whether to be affected by strength multiplier.")
    overrideSeconds: float = Field(
        description="The number of seconds to override the strength.", ge=0.5, le=5
    )


class WindOverride(BaseModel):
    id: str = Field(description="The ID of the parameter to override the wind of.")
    value: float = Field(description="The value of the wind override.", ge=0, le=100)
    setBaseValue: bool = Field(description="Whether to be affected by wind multiplier.")
    overrideSeconds: float = Field(
        description="The number of seconds to override the wind.", ge=0.5, le=5
    )


class SetCurrentModelPhysicsRequestData(BaseModel):
    """Data for authentication request."""

    strengthOverrides: List[StrengthOverride] = Field([], description="The strength overrides.")
    windOverrides: List[WindOverride] = Field([], description="The wind overrides.")


class SetCurrentModelPhysicsRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.SetCurrentModelPhysicsRequest] = (
        MessageType.SetCurrentModelPhysicsRequest
    )
    data: SetCurrentModelPhysicsRequestData


class SetCurrentModelPhysicsResponseData(BaseModel):
    """Data for authentication response."""


class SetCurrentModelPhysicsResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.SetCurrentModelPhysicsResponse] = (
        MessageType.SetCurrentModelPhysicsResponse
    )
    data: Union[SetCurrentModelPhysicsResponseData, ErrorData]


# ============================================================================
# NDI
# ============================================================================


class NDIConfigRequestData(BaseModel):
    """Data for authentication request."""

    setNewConfig: bool
    ndiActive: bool = Field(False, description="Whether to set NDI as active.")
    useNDI5: bool = Field(True, description="Whether to use NDI 5.")
    useCustomResolution: bool = Field(False, description="Whether to use a custom resolution.")
    customWidthNDI: int = Field(
        -1,
        description="The width of the custom resolution.",
        validate_default=False,
        ge=256,
        le=8192,
    )
    customHeightNDI: int = Field(
        -1,
        description="The height of the custom resolution.",
        validate_default=False,
        ge=256,
        le=8192,
    )


class NDIConfigRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.NDIConfigRequest] = MessageType.NDIConfigRequest
    data: NDIConfigRequestData


class NDIConfigResponseData(BaseModel):
    """Data for authentication response."""

    setNewConfig: bool
    ndiActive: bool
    useNDI5: bool
    useCustomResolution: bool
    customWidthNDI: int
    customHeightNDI: int


class NDIConfigResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.NDIConfigResponse] = MessageType.NDIConfigResponse
    data: Union[NDIConfigResponseData, ErrorData]


# ============================================================================
# Items Get List
# ============================================================================


class ItemListRequestData(BaseModel):
    """Data for authentication request."""

    includeAvailableSpots: bool = Field(False, description="Whether to include available spots.")
    includeItemInstancesInScene: bool = Field(
        False, description="Whether to include item instances in scene."
    )
    includeAvailableItemFiles: bool = Field(
        False, description="Whether to include available item files."
    )
    onlyItemsWithFileName: Optional[str] = Field(
        None, description="The file name of the item to get the list of."
    )
    onlyItemsWithInstanceID: Optional[str] = Field(
        None, description="The instance ID of the item to get the list of."
    )


class ItemListRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ItemListRequest] = MessageType.ItemListRequest
    data: ItemListRequestData


class ItemListResponseData(BaseModel):
    """Data for authentication response."""

    itemsInSceneCount: int
    totalItemsAllowedCount: int
    canLoadItemsRightNow: bool
    availableSpots: List[int]
    itemInstancesInScene: List[ItemInstance]
    availableItemFiles: List[ItemFile]


class ItemListResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ItemListResponse] = MessageType.ItemListResponse
    data: Union[ItemListResponseData, ErrorData]


# ============================================================================
# Item Load
# ============================================================================


class ItemLoadRequestData(BaseModel):
    """Data for authentication request."""

    fileName: str = Field(description="The file name of the item to load.")
    positionX: float = Field(
        0, description="The X position of the item to load.", ge=-1000, le=1000
    )
    positionY: float = Field(
        0, description="The Y position of the item to load.", ge=-1000, le=1000
    )
    size: float = Field(1, description="The size of the item to load.", ge=0, le=1)
    rotation: float = Field(0, description="The rotation of the item to load.", ge=-360, le=360)
    fadeTime: float = Field(0.25, description="The fade time of the item to load.", ge=0, le=2)
    order: int = Field(0, description="The order of the item to load.")
    failIfOrderTaken: bool = Field(False, description="Whether to fail if the order is taken.")
    smoothing: float = Field(0.5, description="The smoothing of the item to load.", ge=0, le=1)
    censored: Optional[bool] = Field(False, description="Whether the item is censored.")
    flipped: Optional[bool] = Field(False, description="Whether the item is flipped.")
    locked: Optional[bool] = Field(False, description="Whether the item is locked.")
    unloadWhenPluginDisconnects: bool = Field(
        True, description="Whether to unload the item when the plugin disconnects."
    )
    customDataBase64: Optional[str] = Field(
        None, description="The custom data of the item to load."
    )
    customDataAskUserFirst: Optional[bool] = Field(
        None, description="Whether to ask the user first if the custom data is available."
    )
    customDataSkipAskingUserIfWhitelisted: Optional[bool] = Field(
        None, description="Whether to skip asking the user if the custom data is whitelisted."
    )
    customDataAskTimer: Optional[int] = Field(
        None, description="The timer to ask the user if the custom data is available."
    )


class ItemLoadRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ItemLoadRequest] = MessageType.ItemLoadRequest
    data: ItemLoadRequestData


class ItemLoadResponseData(BaseModel):
    """Data for authentication response."""

    instanceID: str
    fileName: str


class ItemLoadResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ItemLoadResponse] = MessageType.ItemLoadResponse
    data: Union[ItemLoadResponseData, ErrorData]


# ============================================================================
# Item Remove
# ============================================================================


class ItemUnloadRequestData(BaseModel):
    """Data for authentication request."""

    unloadAllInScene: bool = Field(False, description="Whether to unload all items in scene.")
    unloadAllLoadedByThisPlugin: bool = Field(
        False, description="Whether to unload all items loaded by this plugin."
    )
    allowUnloadingItemsLoadedByUserOrOtherPlugins: bool = Field(
        False, description="Whether to allow unloading items loaded by user or other plugins."
    )
    instanceIDs: List[str] = Field([], description="The instance IDs of the items to unload.")
    fileNames: List[str] = Field([], description="The file names of the items to unload.")


class ItemUnloadRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ItemUnloadRequest] = MessageType.ItemUnloadRequest
    data: ItemUnloadRequestData


class ItemUnloadedItem(BaseModel):
    instanceID: str
    fileName: str


class ItemUnloadResponseData(BaseModel):
    """Data for authentication response."""

    unloadedItems: List[ItemUnloadedItem]


class ItemUnloadResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ItemUnloadResponse] = MessageType.ItemUnloadResponse
    data: Union[ItemUnloadResponseData, ErrorData]


# ============================================================================
# Item Control
# ============================================================================


class ItemAnimationControlRequestData(BaseModel):
    """Data for authentication request."""

    itemInstanceID: str
    framerate: float = Field(
        -1, description="The framerate of the animation.", validate_default=False, ge=0.1, le=120
    )
    frame: int = Field(-1, description="The frame of the animation.", validate_default=False, ge=0)
    brightness: float = Field(
        -1, description="The brightness of the animation.", validate_default=False, ge=0, le=1
    )
    opacity: float = Field(
        -1, description="The opacity of the animation.", validate_default=False, ge=0, le=1
    )
    setAutoStopFrames: bool = Field(False, description="Whether to set the auto stop frames.")
    autoStopFrames: List[int] = Field([], description="The frames to auto stop at.", max_items=1024)
    setAnimationPlayState: bool = Field(
        True, description="Whether to set the animation play state."
    )
    animationPlayState: bool = Field(True, description="Whether the animation is playing.")


class ItemAnimationControlRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ItemAnimationControlRequest] = (
        MessageType.ItemAnimationControlRequest
    )
    data: ItemAnimationControlRequestData


class ItemAnimationControlResponseData(BaseModel):
    """Data for authentication response."""

    frame: int
    animationPlaying: bool


class ItemAnimationControlResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ItemAnimationControlResponse] = (
        MessageType.ItemAnimationControlResponse
    )
    data: Union[ItemAnimationControlResponseData, ErrorData]


# ============================================================================
# Item Move
# ============================================================================


class FadeMode(Enum):
    LINEAR = "linear"
    EASEIN = "easeIn"
    EASEOUT = "easeOut"
    EASEBOTH = "easeBoth"
    OVERSHOOT = "overshoot"
    ZIP = "zip"


class ItemMoveRequestItem(BaseModel):
    itemInstanceID: str = Field(description="The instance ID of the item.")
    timeInSeconds: float = Field(
        1, description="The time in seconds to move the item.", ge=0, le=30
    )
    fadeMode: FadeMode = Field(FadeMode.EASEBOTH, description="The fade mode of the item.")
    positionX: float = Field(0, description="The X position of the item.", ge=-1000, le=1000)
    positionY: float = Field(0, description="The Y position of the item.", ge=-1000, le=1000)
    size: float = Field(1, description="The size of the item.", ge=0, le=1)
    rotation: float = Field(0, description="The rotation of the item.", ge=-360, le=360)
    order: int = Field(-1000, description="The order of the item.")
    setFlip: bool = Field(False, description="Whether to set the flip.")
    flip: bool = Field(True, description="Whether to flip the item.")
    userCanStop: bool = Field(True, description="Whether the user can stop the item.")


class ItemMoveRequestData(BaseModel):
    """Data for authentication request."""

    itemsToMove: List[ItemMoveRequestItem] = Field(description="The items to move.", max_items=64)


class ItemMoveRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ItemMoveRequest] = MessageType.ItemMoveRequest
    data: ItemMoveRequestData


class MovedItem(BaseModel):
    itemInstanceID: str
    success: bool
    errorID: int


class ItemMoveResponseData(BaseModel):
    """Data for authentication response."""

    movedItems: List[MovedItem]


class ItemMoveResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ItemMoveResponse] = MessageType.ItemMoveResponse
    data: Union[ItemMoveResponseData, ErrorData]


# ============================================================================
# Within-Model-Sorting Items
# ============================================================================


class ItemSplitPoint(Enum):
    UNCHANGED = "Unchanged"
    ARTMESHID = "UseArtMeshID"


class ItemSortOrder(Enum):
    UNCHANGED = "Unchanged"
    ARTMESHID = "UseArtMeshID"
    SPECIALID = "UseSpecialID"


class WithinModelOrder(Enum):
    FULLYINFRONT = "FullyInFront"
    FULLYINBACK = "FullyInBack"


class ItemSortRequestData(BaseModel):  # TODO specialized builder for this model
    """Data for authentication request."""

    itemInstanceID: str
    frontOn: bool
    backOn: bool
    setSplitPoint: ItemSplitPoint
    setFrontOrder: ItemSortOrder
    setBackOrder: ItemSortOrder
    splitAt: str
    withinModelOrderFront: WithinModelOrder
    withinModelOrderBack: WithinModelOrder


class ItemSortRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ItemSortRequest] = MessageType.ItemSortRequest
    data: ItemSortRequestData


class ItemSortResponseData(BaseModel):
    """Data for authentication response."""

    itemInstanceID: str
    modelLoaded: bool
    modelID: str
    modelName: str
    loadedModelHadRequestedFrontLayer: bool
    loadedModelHadRequestedBackLayer: bool


class ItemSortResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ItemSortResponse] = MessageType.ItemSortResponse
    data: Union[ItemSortResponseData, ErrorData]


# ============================================================================
# Ask User Select Artmesh
# ============================================================================


class ArtMeshSelectionRequestData(BaseModel):
    """Data for authentication request."""

    textOverride: Optional[str] = Field(
        None, description="The text override.", min_length=4, max_length=1024
    )
    helpOverride: Optional[str] = Field(
        None, description="The help override.", min_length=4, max_length=1024
    )
    requestedArtMeshCount: int = Field(0, description="The requested art mesh count.", ge=0)
    activeArtMeshes: List[str] = Field([], description="The pre-active art meshes.")


class ArtMeshSelectionRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ArtMeshSelectionRequest] = MessageType.ArtMeshSelectionRequest
    data: ArtMeshSelectionRequestData


class ArtMeshSelectionResponseData(BaseModel):
    """Data for authentication response."""

    success: bool
    activeArtMeshes: List[str]
    inactiveArtMeshes: List[str]


class ArtMeshSelectionResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ArtMeshSelectionResponse] = (
        MessageType.ArtMeshSelectionResponse
    )
    data: Union[ArtMeshSelectionResponseData, ErrorData]


# ============================================================================
# Pin Items
# ============================================================================


class AngleRelativeTo(Enum):
    RELATIVE_TO_WORLD = "RelativeToWorld"
    RELATIVE_TO_CURRENT_ITEM_ROTATION = "RelativeToCurrentItemRotation"
    RELATIVE_TO_MODEL = "RelativeToModel"
    RELATIVE_TO_PIN_POSITION = "RelativeToPinPosition"


class SizeRelativeTo(Enum):
    RELATIVE_TO_MODEL = "RelativeToModel"
    RELATIVE_TO_CURRENT_ITEM_SIZE = "RelativeToCurrentItemSize"


class VertexPinType(Enum):
    PROVIDED = "Provided"
    CENTER = "Center"
    RANDOM = "Random"


class PinInfo(BaseModel):
    modelID: str = Field(description="The model ID.")
    artMeshID: str = Field(description="The art mesh ID.")
    angle: float = Field(0, description="The angle.", ge=-360, le=360)
    size: float = Field(1, description="The size.", ge=0, le=1)
    vertexID1: Optional[int] = Field(None, description="The vertex ID 1.")
    vertexID2: Optional[int] = Field(None, description="The vertex ID 2.")
    vertexID3: Optional[int] = Field(None, description="The vertex ID 3.")
    vertexWeight1: Optional[float] = Field(None, description="The vertex weight 1.")
    vertexWeight2: Optional[float] = Field(None, description="The vertex weight 2.")
    vertexWeight3: Optional[float] = Field(None, description="The vertex weight 3.")


class ItemPinRequestData(BaseModel):  # TODO specialized builder for this model
    """Data for authentication request."""

    pin: bool = Field(description="Whether to pin the item.")
    itemInstanceID: str = Field(description="The item instance ID.")
    angleRelativeTo: AngleRelativeTo = Field(
        AngleRelativeTo.RELATIVE_TO_MODEL, description="The angle relative to."
    )
    sizeRelativeTo: SizeRelativeTo = Field(
        SizeRelativeTo.RELATIVE_TO_MODEL, description="The size relative to."
    )
    vertexPinType: VertexPinType = Field(VertexPinType.CENTER, description="The vertex pin type.")
    pinInfo: PinInfo = Field(description="The pin info.")


class ItemPinRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ItemPinRequest] = MessageType.ItemPinRequest
    data: ItemPinRequestData


class ItemPinResponseData(BaseModel):
    """Data for authentication response."""

    isPinned: bool
    itemInstanceID: str
    itemFileName: str


class ItemPinResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ItemPinResponse] = MessageType.ItemPinResponse
    data: Union[ItemPinResponseData, ErrorData]


# ============================================================================
# Post Processing Get List
# ============================================================================


class PostProcessingListRequestData(BaseModel):
    """Data for authentication request."""

    fillPostProcessingPresetsArray: bool = Field(
        False, description="Whether to fill the post processing presets array."
    )
    fillPostProcessingEffectsArray: bool = Field(
        False, description="Whether to fill the post processing effects array."
    )
    effectIDFilter: List[PostProcessingEffect] = Field([], description="The effect ID filter.")


class PostProcessingListRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.PostProcessingListRequest] = (
        MessageType.PostProcessingListRequest
    )
    data: PostProcessingListRequestData


class PostProcessingEffectConfigInfo(BaseModel):
    internalID: str
    enumID: PostProcessingEffectConfigID
    explanation: str
    type: str
    activationConfig: bool
    floatValue: float
    floatMin: float
    floatMax: float
    floatDefault: float
    intValue: int
    intMin: int
    intMax: int
    intDefault: int
    colorValue: str
    colorDefault: str
    colorHasAlpha: bool
    boolValue: bool
    boolDefault: bool
    stringValue: str
    stringDefault: str
    sceneItemValue: str
    sceneItemDefault: str


class PostProcessingEffectInfo(BaseModel):
    internalID: str
    enumID: str
    explanation: str
    effectIsActive: bool
    effectIsRestricted: bool
    configEntries: List[PostProcessingEffectConfigInfo]


class PostProcessingListResponseData(BaseModel):
    """Data for authentication response."""

    postProcessingSupported: bool
    postProcessingActive: bool
    canSendPostProcessingUpdateRequestRightNow: bool
    restrictedEffectsAllowed: bool
    presetIsActive: bool
    activePreset: str
    presetCount: int
    activeEffectCount: int
    effectCountBeforeFilter: int
    configCountBeforeFilter: int
    effectCountAfterFilter: int
    configCountAfterFilter: int
    postProcessingEffects: List[PostProcessingEffectInfo]
    postProcessingPresets: List[str]


class PostProcessingListResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.PostProcessingListResponse] = (
        MessageType.PostProcessingListResponse
    )
    data: Union[PostProcessingListResponseData, ErrorData]


# ============================================================================
# Post Processing Set
# ============================================================================


class PostProcessingUpdateValue(BaseModel):
    configID: PostProcessingEffectConfigID = Field(description="The config ID.")
    configValue: str = Field(description="The config value as a string.")


class PostProcessingUpdateRequestData(BaseModel):
    """Data for authentication request."""

    postProcessingOn: bool = Field(False, description="Whether to turn on the post processing.")
    setPostProcessingPreset: bool = Field(
        False, description="Whether to set the post processing preset."
    )
    setPostProcessingValues: bool = Field(
        False, description="Whether to set the post processing values."
    )
    presetToSet: Optional[str] = Field(None, description="The preset to set.")
    postProcessingFadeTime: float = Field(
        0.25, description="The post processing fade time.", ge=0, le=2
    )
    setAllOtherValuesToDefault: bool = Field(
        False, description="Whether to set all other values to default."
    )
    usingRestrictedEffects: bool = Field(False, description="Whether to use restricted effects.")
    randomizeAll: bool = Field(False, description="Whether to randomize all.")
    randomizeAllChaosLevel: float = Field(
        0.5, description="The randomize all chaos level.", ge=0, le=1
    )
    postProcessingValues: List[PostProcessingUpdateValue] = Field(
        [], description="The post processing values."
    )


class PostProcessingUpdateRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.PostProcessingUpdateRequest] = (
        MessageType.PostProcessingUpdateRequest
    )
    data: PostProcessingUpdateRequestData


class PostProcessingUpdateResponseData(BaseModel):
    """Data for authentication response."""

    postProcessingActive: bool
    presetIsActive: bool
    activePreset: str
    activeEffectCount: int


class PostProcessingUpdateResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.PostProcessingUpdateResponse] = (
        MessageType.PostProcessingUpdateResponse
    )
    data: Union[PostProcessingUpdateResponseData, ErrorData]
