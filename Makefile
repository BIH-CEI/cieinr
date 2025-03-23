.PHONY: install test lint bump-version-patch bump-version-minor bump-version-major help

# Get version from Python code
VERSION := $(shell python -c "from cieinr._version import __version__; print(__version__)")

help:
	@echo "CIEINR Makefile"
	@echo "--------------"
	@echo "make install           Install the package for development"
	@echo "make test              Run tests"
	@echo "make lint              Run linters and code quality tools"
	@echo "make bump-version-patch  Bump patch version (1.0.0 -> 1.0.1)"
	@echo "make bump-version-minor  Bump minor version (1.0.0 -> 1.1.0)"
	@echo "make bump-version-major  Bump major version (1.0.0 -> 2.0.0)"
	@echo ""
	@echo "Current version: $(VERSION)"

install:
	pip install -e ".[dev]"

test:
	python -m pytest

lint:
	python -m ruff check .

bump-version-patch:
	@echo "Bumping patch version..."
	python scripts/bump_version.py patch

bump-version-minor:
	@echo "Bumping minor version..."
	python scripts/bump_version.py minor

bump-version-major:
	@echo "Bumping major version..."
	python scripts/bump_version.py major