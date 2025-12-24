# Documentation

This directory contains documentation for vtube-python.

## Requirements

To build the documentation, install the development dependencies:

```bash
pip install -e ".[dev]"
```

This includes Sphinx and the Read the Docs theme.

## Building Documentation

Documentation can be built using Sphinx:

```bash
cd docs
sphinx-build -b html . _build/html
```

The built documentation will be available in `docs/_build/html/index.html`.

## Documentation Structure

- **Getting Started**: Installation and basic usage guide
- **Guides**: Detailed guides for common use cases:
  - Connection management
  - Event handling
  - Working with models
  - Hotkeys
  - Parameters
  - Items
- **API Reference**: Complete API documentation auto-generated from docstrings
- **Examples**: Code examples with explanations

