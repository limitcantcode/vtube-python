# AI Agents Guide

This document provides guidance for AI agents (like GitHub Copilot, ChatGPT, Cursor, etc.) working on this codebase.

## Project Overview

**vtube-python** (vtpy) is a Python library for interfacing with VTube Studio's WebSocket API. VTube Studio is a desktop application that allows users to control Live2D avatars using face tracking.

## Key Technologies

- **Python 3.8+**: The library supports Python 3.8 and above
- **WebSockets**: Communication with VTube Studio uses WebSocket protocol
- **Async/Await**: The library uses asyncio for asynchronous operations
- **VTube Studio API**: Based on the official API documentation at https://github.com/DenchiSoft/VTubeStudio

## Architecture Principles

1. **Async-First**: All API calls should be asynchronous using `async/await`
2. **Type Hints**: Use type hints throughout the codebase for better IDE support
3. **Error Handling**: Provide clear, actionable error messages
4. **Documentation**: Include docstrings for all public classes and methods
5. **Testing**: Write tests for all new features

## Code Style

- Follow PEP 8 guidelines
- Use Black for code formatting (line length: 100)
- Use Ruff for linting
- Use type hints with `typing` module
- Prefer `f-strings` for string formatting

## Common Patterns

### API Request Pattern

```python
async def api_method(self, param: str) -> ResponseType:
    """Method description.
    
    Args:
        param: Parameter description
        
    Returns:
        Response description
        
    Raises:
        VTubeStudioError: Error description
    """
    request = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": "1.0",
        "requestID": self._generate_request_id(),
        "messageType": "RequestType",
        "data": {
            "param": param
        }
    }
    response = await self._send_request(request)
    return ResponseType.from_dict(response["data"])
```

### Error Handling

```python
from vtpy.exceptions import VTubeStudioError

if not response.get("data"):
    raise VTubeStudioError(f"Invalid response: {response}")
```

## Testing Guidelines

- Place tests in the `tests/` directory
- Use pytest with pytest-asyncio for async tests
- Mock WebSocket connections in tests
- Aim for >80% code coverage

## Resources

- [VTube Studio API Documentation](https://github.com/DenchiSoft/VTubeStudio)
- [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455)

## When Adding New Features

1. Check the VTube Studio API documentation for the endpoint
2. Create a corresponding method in the appropriate class
3. Add type hints and docstrings
4. Write tests
5. Update documentation if needed
6. Follow the existing code patterns

