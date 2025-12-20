# Contributing to vtube-python

Thank you for your interest in contributing to vtube-python! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How to Contribute

### Reporting Bugs

Before creating a bug report, please:
1. Check if the issue has already been reported in the [Issues](https://github.com/limitcantcode/vtube-python/issues) section
2. Check the [VTube Studio API documentation](https://github.com/DenchiSoft/VTubeStudio) to ensure the behavior is expected

When creating a bug report, please include:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Python version and operating system
- VTube Studio version (if applicable)
- Any relevant error messages or logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:
1. Check if the enhancement has already been suggested
2. Provide a clear description of the proposed enhancement
3. Explain why this enhancement would be useful
4. Provide examples of how it would be used

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding standards below
3. **Add tests** for new functionality
4. **Update documentation** as needed
5. **Ensure all tests pass** and code is properly formatted
6. **Submit the pull request** with a clear description of changes

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip
- (Optional) VTube Studio for testing

### Installation

1. Clone your fork:
   ```bash
   git clone https://github.com/your-username/vtube-python.git
   cd vtube-python
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the project in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

### Running Tests

```bash
pytest
```

To run with coverage:
```bash
pytest --cov=vtpy --cov-report=html
```

### Code Formatting

Format code with Black:
```bash
black vtpy tests examples
```

### Linting

Check code with Ruff:
```bash
ruff check vtpy tests
```

Auto-fix issues:
```bash
ruff check --fix vtpy tests
```

### Type Checking

Run mypy:
```bash
mypy vtpy
```

## Coding Standards

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use Black for formatting (line length: 100)
- Use type hints for all function signatures
- Write docstrings for all public classes and methods

### Code Structure

- Keep functions focused and single-purpose
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions reasonably short

### Documentation

- Use Google-style docstrings
- Include type information in docstrings
- Document all public APIs
- Update README.md for user-facing changes

### Testing

- Write tests for all new features
- Aim for >80% code coverage
- Use descriptive test names
- Test both success and error cases

## Commit Messages

Write clear, descriptive commit messages:
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests when applicable

Example:
```
Add support for expression activation API

Implements the ExpressionActivationRequest endpoint from VTube Studio API.
Includes tests and documentation updates.

Fixes #123
```

## Project Structure

```
vtube-python/
├── vtpy/              # Main package
├── tests/             # Test files
├── examples/          # Example scripts
├── docs/             # Documentation
├── .github/          # GitHub templates and workflows
└── README.md         # Project README
```

## Questions?

If you have questions about contributing, please:
- Open an issue with the "question" label
- Check existing issues and discussions
- Review the [VTube Studio API documentation](https://github.com/DenchiSoft/VTubeStudio)

Thank you for contributing to vtube-python!

