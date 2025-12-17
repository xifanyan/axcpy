#!/bin/bash
# Development environment setup script using uv

set -e

echo "Setting up axcpy development environment..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
else
    echo "✓ uv is already installed"
fi

# Set Python version
echo "Setting Python version..."
echo "3.11" > .python-version

# Sync dependencies
echo "Installing dependencies..."
uv sync --all-extras

# Install pre-commit hooks (if available)
if [ -f ".pre-commit-config.yaml" ]; then
    echo "Installing pre-commit hooks..."
    uv run pre-commit install
fi

echo ""
echo "✓ Development environment setup complete!"
echo ""
echo "Next steps:"
echo "  1. Activate the virtual environment: source .venv/bin/activate"
echo "  2. Run tests: uv run pytest"
echo "  3. Run CLI: uv run axcpy --help"
echo "  4. Start coding!"
