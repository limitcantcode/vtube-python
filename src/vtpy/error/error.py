from vtpy.data.common import ErrorCode


class VTSRequestError(Exception):
    def __init__(self, message: str, error_id: ErrorCode):
        super().__init__(message)
        self.error_id = error_id
        self.message = message

    def __str__(self) -> str:
        return f"[{self.error_id.name}]({self.error_id}): {self.message}"

    def __repr__(self) -> str:
        return f"VTSRequestError(error_id={self.error_id.name}, message={self.message})"
