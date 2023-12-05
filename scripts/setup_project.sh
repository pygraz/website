#!/bin/sh
set -e
echo "🧱 Installing project"
poetry install
echo "🛠️ Installing pre-commit"
poetry run pre-commit install
echo "🎉 Successfully set up project"
