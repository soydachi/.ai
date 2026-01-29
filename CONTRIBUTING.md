# Contributing to AI Way of Working (ai-wow)

Thank you for your interest in contributing to ai-wow! This document provides guidelines and information for contributors.

## Development Setup

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Setting Up the Development Environment

```bash
# Clone the repository
git clone https://github.com/soydachi/ai-wow.git
cd ai-wow

# Create a virtual environment (recommended)
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Verify installation
ai-wow --version
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=ai_wow

# Run specific test file
pytest tests/test_cli.py
```

### Code Quality

```bash
# Format code
ruff format src/

# Lint code
ruff check src/

# Type checking
mypy src/
```

## Project Structure

```
ai-wow/
├── src/ai_wow/           # Main package
│   ├── cli.py            # Main CLI entry point
│   ├── commands/         # CLI commands
│   │   ├── init.py       # ai-wow init
│   │   ├── sync.py       # ai-wow sync
│   │   ├── validate.py   # ai-wow validate
│   │   └── update.py     # ai-wow update
│   ├── utils/            # Utility modules
│   │   ├── console.py    # Terminal output helpers
│   │   └── paths.py      # Path utilities
│   └── templates/        # Template files for init
├── tests/                # Test files
├── .github/workflows/    # CI/CD pipelines
├── install.sh            # Linux/macOS installer
├── install.ps1           # Windows installer
└── pyproject.toml        # Package configuration
```

## Making Changes

### Adding a New Command

1. Create a new file in `src/ai_wow/commands/`
2. Use Click decorators for CLI options
3. Register the command in `src/ai_wow/cli.py`
4. Add tests in `tests/`

### Adding a New Stack

1. Add the stack to the `StackType` literal in `src/ai_wow/commands/init.py`
2. Update the Click choice options
3. Add stack-specific templates if needed
4. Update documentation

### Modifying Templates

Templates are used by `ai-wow init` to create the `.ai/` structure:
- Basic templates are created programmatically in `commands/init.py`
- Complex templates can be added to `src/ai_wow/templates/`

## Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests: `pytest`
5. Run linting: `ruff check src/`
6. Commit your changes: `git commit -m 'Add amazing feature'`
7. Push to the branch: `git push origin feature/amazing-feature`
8. Open a Pull Request

### PR Guidelines

- Keep changes focused and atomic
- Include tests for new functionality
- Update documentation as needed
- Follow existing code style
- Ensure CI passes

## Release Process

Releases are automated via GitHub Actions:

1. Update version in `src/ai_wow/__init__.py`
2. Update version in `pyproject.toml`
3. Create a GitHub release with tag `v{version}`
4. The CI/CD pipeline will automatically publish to PyPI

## Code Style

- Follow PEP 8 guidelines
- Use type hints for function signatures
- Write docstrings for public functions
- Keep functions focused and small
- Use meaningful variable names

## Questions?

If you have questions or need help, please:
- Open an issue on GitHub
- Check existing issues for similar questions
- Review the documentation

Thank you for contributing! 🎉
