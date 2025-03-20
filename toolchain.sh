#!/bin/bash

echo "Setting up Python environment with Poetry..."

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry not found. Installing Poetry..."
    pip install poetry
fi

# Install dependencies and set up virtual environment
poetry install

echo "Environment successfully set up and ready to use."
echo "Use the following commands to run tests and main.py:"
echo "  To run tests: poetry run pytest python_lib/interest_rate_models/tests"
echo "  To run main: poetry run python python_lib/interest_rate_models/main.py"

