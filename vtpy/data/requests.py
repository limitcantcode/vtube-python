"""Request and response data models for VTube Studio API."""

from email.policy import strict
from typing import Optional, List, Dict, Any, Literal, Union
from enum import Enum
from pydantic import BaseModel
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
    "ModelLoadRequestRequestData",
    "ModelLoadRequestRequest",
    "ModelLoadRequestResponseData",
    "ModelLoadRequestResponse",
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
    "InputParamaterListRequestData",
    "InputParamaterListRequest",
    "InputParamaterListResponseData",
    "InputParamaterListResponse",
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
    "ParamaterDeletionRequestData",
    "ParamaterDeletionRequest",
    "ParamaterDeletionResponseData",
    "ParamaterDeletionResponse",
    "ParameterValue",
    "InjectParameterDataRequestData",
    "InjectParameterDataRequest",
    "InjectParameterDataResponseData",
    "GetCurrentModelRequestData",
    "GetCurrentModelRequest",
    "PhysicsGroup",
    "GetCurrentModelResponseData",
    "GetCurrentModelResponse",
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
    "ItemAnimationControlRequestRequestData",
    "ItemAnimationControlRequestRequest",
    "ItemAnimationControlRequestResponseData",
    "ItemAnimationControlRequestResponse",
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

    requestedPermission: PermissionType


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

    pluginName: str
    pluginDeveloper: str
    authenticationToken: str


class AuthenticationRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.AuthenticationTokenRequest] = (
        MessageType.AuthenticationTokenRequest
    )
    data: AuthenticationRequestData


class AuthenticationResponseData(BaseModel):
    """Data for authentication response."""

    authenticated: bool
    reason: Optional[str] = None


class AuthenticationResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.AuthenticationTokenResponse] = (
        MessageType.AuthenticationTokenResponse
    )
    data: Union[AuthenticationResponseData, ErrorData]


# ============================================================================
# Authentication Get Token
# ============================================================================


class AuthenticationTokenRequestData(BaseModel):
    """Data for authentication request."""

    pluginName: str
    pluginDeveloper: str
    pluginIcon: Optional[str] = None


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


class ModelLoadRequestRequestData(BaseModel):
    """Data for authentication request."""

    modelID: str


class ModelLoadRequestRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ModelLoadRequest] = MessageType.ModelLoadRequest
    data: ModelLoadRequestRequestData


class ModelLoadRequestResponseData(BaseModel):
    """Data for authentication response."""

    modelID: str


class ModelLoadRequestResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ModelLoadRequestResponse] = (
        MessageType.ModelLoadRequestResponse
    )
    data: Union[ModelLoadRequestResponseData, ErrorData]


# ============================================================================
# Move Model
# ============================================================================


class MoveModelRequestData(BaseModel):
    """Data for authentication request."""

    timeInSeconds: float
    valuesAreRelativeToModel: bool
    positionX: float
    positionY: float
    rotation: float
    size: float


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

    modelID: str
    live2DItemFileName: str


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

    hotkeyID: str
    itemInstanceID: str


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

    details: bool
    expressionFile: str


class ExpressionStateRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ExpressionStateRequest] = MessageType.ExpressionStateRequest
    data: ExpressionStateRequestData


class Hotkey(BaseModel):
    name: str
    id: str


class Parameter(BaseModel):
    name: str
    value: int


class Expression(BaseModel):
    name: str
    file: str
    active: bool
    deactivateWhenKeyIsLetGo: bool
    autoDeactivateAfterSeconds: bool
    secondsRemaining: int
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

    expressionFile: str
    fadeTime: float
    active: bool


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
    colorR: int
    colorG: int
    colorB: int
    colorA: int
    mixWithSceneLightingColor: int


class ArtMeshMatcherData(BaseModel):
    tintAll: bool
    artMeshNumber: List[int]
    nameExact: List[str]
    nameContains: List[str]
    tagExact: List[str]
    tagContains: List[str]


class ColorTintRequestData(BaseModel):
    """Data for authentication request."""

    colorTint: ColorTintData
    artMeshMatcher: ArtMeshMatcherData


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


class InputParamaterListRequestData(BaseModel):
    """Data for authentication request."""


class InputParamaterListRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.InputParameterListRequest] = (
        MessageType.InputParameterListRequest
    )
    data: InputParamaterListRequestData


class InputParamaterListResponseData(BaseModel):
    """Data for authentication response."""

    modelLoaded: bool
    modelName: str
    modelID: str
    customParameters: List[Parameter]
    defaultParameters: List[Parameter]


class InputParamaterListResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.InputParameterListResponse] = (
        MessageType.InputParameterListResponse
    )
    data: Union[InputParamaterListResponseData, ErrorData]


# ============================================================================
# Parameter Value Get
# ============================================================================


class ParameterValueRequestData(BaseModel):
    """Data for authentication request."""

    name: str


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

    parameterName: str
    explanation: str
    min: float
    max: float
    defaultValue: float


class ParameterCreationRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ParameterCreateRequest] = MessageType.ParameterCreateRequest
    data: ParameterCreationRequestData


class ParameterCreationResponseData(BaseModel):
    """Data for authentication response."""

    parameterName: str


class ParameterCreationResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ParameterCreateResponse] = MessageType.ParameterCreateResponse
    data: Union[ParameterCreationResponseData, ErrorData]


# ============================================================================
# Parameter Delete
# ============================================================================


class ParamaterDeletionRequestData(BaseModel):
    """Data for authentication request."""

    parameterName: str


class ParamaterDeletionRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ParameterDeleteRequest] = MessageType.ParameterDeleteRequest
    data: ParamaterDeletionRequestData


class ParamaterDeletionResponseData(BaseModel):
    """Data for authentication response."""

    parameterName: str


class ParamaterDeletionResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ParameterDeleteResponse] = MessageType.ParameterDeleteResponse
    data: Union[ParamaterDeletionResponseData, ErrorData]


# ============================================================================
# Parameter Set
# ============================================================================


class ParameterMode(Enum):
    SET = "set"
    ADD = "add"


class ParameterValue(BaseModel):
    id: str
    value: float
    weight: Optional[float] = None


class InjectParameterDataRequestData(BaseModel):
    """Data for authentication request."""

    faceFound: bool
    mode: ParameterMode
    parameterValues: List[ParameterValue]


class InjectParameterDataRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.InjectParameterDataRequest] = (
        MessageType.InjectParameterDataRequest
    )
    data: InjectParameterDataRequestData


class InjectParameterDataResponseData(BaseModel):
    """Data for authentication response."""


class AuthenticationResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.InjectParameterDataResponse] = (
        MessageType.InjectParameterDataResponse
    )
    data: Union[InjectParameterDataResponseData, ErrorData]


# ============================================================================
# Physics Get
# ============================================================================


class GetCurrentModelRequestData(BaseModel):
    """Data for authentication request."""


class GetCurrentModelRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.GetCurrentModelRequest] = MessageType.GetCurrentModelRequest
    data: GetCurrentModelRequestData


class PhysicsGroup(BaseModel):
    groupID: str
    groupName: str
    strengthMultiplier: float
    windMultiplier: float


class GetCurrentModelResponseData(BaseModel):
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


class GetCurrentModelResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.GetCurrentModelResponse] = MessageType.GetCurrentModelResponse
    data: Union[GetCurrentModelResponseData, ErrorData]


# ============================================================================
# Physics Set
# ============================================================================


class StrengthOverride(BaseModel):
    id: str
    value: float
    setBaseValue: bool
    overrideSeconds: int


class WindOverride(BaseModel):
    id: str
    value: float
    setBaseValue: bool
    overrideSeconds: int


class SetCurrentModelPhysicsRequestData(BaseModel):
    """Data for authentication request."""

    strengthOverrides: List[StrengthOverride]
    windOverrides: List[WindOverride]


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
    ndiActive: bool
    useNDI5: bool
    useCustomResolution: bool
    customWidthNDI: int
    customHeightNDI: int


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

    includeAvailableSpots: bool
    includeItemInstancesInScene: bool
    includeAvailableItemFiles: bool
    onlyItemsWithFileName: str
    onlyItemsWithInstanceID: str


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

    fileName: str
    positionX: float
    positionY: float
    size: float
    rotation: float
    fadeTime: float
    order: int
    failIfOrderTaken: bool
    smoothing: float
    censored: bool
    flipped: bool
    locked: bool
    unloadWhenPluginDisconnects: bool
    customDataBase64: str
    customDataAskUserFirst: bool
    customDataSkipAskingUserIfWhitelisted: bool
    customDataAskTimer: int


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

    unloadAllInScene: bool
    unloadAllLoadedByThisPlugin: bool
    allowUnloadingItemsLoadedByUserOrOtherPlugins: bool
    instanceIDs: List[str]
    fileNames: List[str]


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


class ItemAnimationControlRequestRequestData(BaseModel):
    """Data for authentication request."""

    itemInstanceID: str
    framerate: int
    frame: int
    brightness: int
    opacity: int
    setAutoStopFrames: bool
    autoStopFrames: List[int]
    setAnimationPlayState: bool
    animationPlayState: bool


class ItemAnimationControlRequestRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.ItemAnimationControlRequest] = (
        MessageType.ItemAnimationControlRequest
    )
    data: ItemAnimationControlRequestRequestData


class ItemAnimationControlRequestResponseData(BaseModel):
    """Data for authentication response."""

    frame: int
    animationPlaying: bool


class ItemAnimationControlRequestResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.ItemAnimationControlRequestResponse] = (
        MessageType.ItemAnimationControlRequestResponse
    )
    data: Union[ItemAnimationControlRequestResponseData, ErrorData]


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
    itemInstanceID: str
    timeInSeconds: float
    fadeMode: FadeMode
    positionX: float
    positionY: float
    size: float
    rotation: float
    order: int
    setFlip: bool
    flip: bool
    userCanStop: bool


class ItemMoveRequestData(BaseModel):
    """Data for authentication request."""

    itemsToMove: List[ItemMoveRequestItem]


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


class ItemSortOrder(ItemSplitPoint):
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

    textOverride: str
    helpOverride: str
    requestedArtMeshCount: int
    activeArtMeshes: List[str]


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
    modelID: str
    artMeshID: str
    angle: float
    size: float
    vertexID1: int
    vertexID2: int
    vertexID3: int


class ItemPinRequestData(BaseModel):  # TODO specialized builder for this model
    """Data for authentication request."""

    pin: bool
    itemInstanceID: str
    angleRelativeTo: str
    sizeRelativeTo: str
    vertexPinType: str
    pinInfo: PinInfo


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

    fillPostProcessingPresetsArray: bool
    fillPostProcessingEffectsArray: bool
    effectIDFilter: List[PostProcessingEffect]


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
    configID: PostProcessingEffectConfigID
    configValue: str


class PostProcessingUpdateRequestData(BaseModel):
    """Data for authentication request."""

    postProcessingOn: bool
    setPostProcessingPreset: bool
    setPostProcessingValues: bool
    presetToSet: str
    postProcessingFadeTime: float
    setAllOtherValuesToDefault: bool
    usingRestrictedEffects: bool
    randomizeAll: bool
    randomizeAllChaosLevel: float
    postProcessingValues: List[PostProcessingUpdateValue]


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
