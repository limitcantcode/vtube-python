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

- [SDK Documentation](https://vtube-python.readthedocs.io/en/latest/)
- [VTubeStudio API](https://github.com/DenchiSoft/VTubeStudio)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Links

- [**Discord**](https://discord.gg/Z8yyEzHsYM)
- [**VTube Studio API Documentation**](https://github.com/DenchiSoft/VTubeStudio)