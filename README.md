<p align="center">
  <img alt="VTube-Python badge" src="https://img.shields.io/badge/VTube-Python-blue">
  <img alt="Github Release" src="https://img.shields.io/github/v/release/limitcantcode/vtube-python" />
  <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/limitcantcode/vtube-python" />
  <img alt="Issues" src="https://img.shields.io/github/issues/limitcantcode/vtube-python" />
  <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/limitcantcode/vtube-python" />
</p>

# vtube-python

Python library for interfacing with VTube Studio's WebSocket API. VTube Studio is a desktop application that allows users to control Live2D avatars using face tracking.

## Features

- 🚀 **Async/Await Support**: Built with Python's `asyncio` for efficient asynchronous operations
- 🔌 **WebSocket Communication**: Direct WebSocket connection to VTube Studio
- 🎭 **Event-Driven**: Subscribe to and handle VTube Studio events in real-time
- 📦 **Type Hints**: Full type hint support for better IDE integration
- 🛡️ **Error Handling**: Comprehensive error handling with clear, actionable messages

## Installation

### Install from PyPI

**NOTE: NOT YET ON PyPI**
```bash
pip install vtube-python
```

### Install from Repository

To install directly from this repository:

```bash
# Clone the repository
git clone https://github.com/limitcantcode/vtube-python.git
cd vtube-python

# Install in development mode
pip install -e .

# Or install normally
pip install .
```

For development with all optional dependencies:

```bash
pip install -e ".[dev]"
```

## Quick Start

### Basic Connection and Authentication

```python
import asyncio
from vtpy import VTS
from vtpy.data.requests import StatisticsRequestData
from vtpy.error import VTSRequestError

async def main():
    # Initialize VTS client
    vts = VTS(plugin_name="MyPlugin", plugin_developer="MyName")
    
    try:
        # Connect to VTube Studio at localhost:8001 and authenticate
        auth_token = await vts.start(host="localhost", port=8001, save_auth_token=False)
        print(f"Successfully authenticated! Token: {auth_token[:20]}...")
        
        # Get VTube Studio statistics
        stats_response = await vts.request_statistics(StatisticsRequestData())
        stats = stats_response.data
        print(f"VTube Studio Version: {stats.vTubeStudioVersion}")
        print(f"Framerate: {stats.framerate} FPS")
        
    except ConnectionError as e:
        print(f"Connection error: {e}")
        print("Make sure VTube Studio is running and the WebSocket API is enabled.")
    except VTSRequestError as e:
        print(f"VTube Studio Request error: {e}")
    finally:
        if vts.connected:
            await vts.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### Listening to Events

```python
import asyncio
from vtpy import VTS
from vtpy.data.events import (
    EventType,
    ModelMovedEvent,
    ModelMovedEventSubscriptionRequestData,
    ModelMovedEventSubscriptionRequestConfig,
)

async def on_model_moved(event: ModelMovedEvent) -> None:
    """Handle model moved events."""
    data = event.data
    position = data.modelPosition
    
    print(f"Model: {data.modelName}")
    print(f"Position: ({position.positionX:.2f}, {position.positionY:.2f})")
    print(f"Rotation: {position.rotation:.2f}°")

async def main():
    vts = VTS(plugin_name="MyPlugin", plugin_developer="MyName")
    
    try:
        # Connect and authenticate
        await vts.start(host="localhost", port=8001, save_auth_token=False)
        
        # Register event handler
        vts.on_event(EventType.ModelMovedEvent, on_model_moved)
        
        # Subscribe to model moved events
        data = ModelMovedEventSubscriptionRequestData(
            subscribe=True, 
            config=ModelMovedEventSubscriptionRequestConfig()
        )
        await vts.event_sub_model_moved(data)
        
        # Keep the connection alive and listen for events
        print("Listening for events. Press Ctrl+C to stop...")
        await asyncio.Event().wait()  # Wait indefinitely
        
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        if vts.connected:
            await vts.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Example Scripts

The repository includes example scripts in the `examples/` directory:

- **`basic_usage.py`**: Demonstrates basic connection, authentication, and retrieving VTube Studio statistics
- **`events_usage.py`**: Shows how to subscribe to and handle VTube Studio events (e.g., model moved events)

To run the examples:

1. Make sure VTube Studio is running with the WebSocket API enabled
2. Install the package (see [Installation](#installation))
3. Run any example:
   ```bash
   python examples/basic_usage.py
   python examples/events_usage.py
   ```

## Documentation

For more detailed documentation, see the [documentation directory](docs/) or check the [VTube Studio API Documentation](https://github.com/DenchiSoft/VTubeStudio).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Links

- [**Discord**](https://discord.gg/Z8yyEzHsYM)
- [**VTube Studio API Documentation**](https://github.com/DenchiSoft/VTubeStudio)