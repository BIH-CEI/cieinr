# CIEINR Project Guidelines

## Development Commands
- Install: `pip install -e .`
- Run tests: `pytest`
- Run specific test: `pytest tests/path/to/test.py::test_function`
- Test with doctests: `pytest --doctest-modules --doctest-glob *.rst`

## Code Style
- Python 3.10+ required
- Imports: stdlib first, third-party second, local packages last
- Types: Use typing annotations consistently
- Naming: CamelCase for classes, snake_case for functions/variables, UPPER_SNAKE_CASE for constants
- Docstrings: Use Google-style with triple quotes
- Error handling: Validate inputs early, use explicit error types and messages

## Project Structure
- Configuration via .env file and singleton Config class
- CLI commands via typer
- Organized by feature modules
- Validation before processing