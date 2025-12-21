# ============================================================================
# API Server Discovery
# ============================================================================


# TODO
class AuthenticationRequestData(BaseModel):
    """Data for authentication request."""

    pluginName: str
    pluginDeveloper: str
    pluginIcon: Optional[str] = None
    authenticationToken: Optional[str] = None


class AuthenticationRequest(BaseRequest):
    """Request to authenticate with VTube Studio."""

    messageType: Literal[MessageType.PermissionRequest] = MessageType.PermissionRequest
    data: AuthenticationRequestData


class AuthenticationResponseData(BaseModel):
    """Data for authentication response."""

    authenticated: bool
    reason: Optional[str] = None


class AuthenticationResponse(BaseResponse):
    """Response from authentication request."""

    messageType: Literal[MessageType.PermissionResponse] = MessageType.PermissionResponse
    data: Union[AuthenticationResponseData, ErrorData]
