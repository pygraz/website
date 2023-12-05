#!/bin/sh
# Update python packages and pre-commit hooks to current versions.
set -e
echo "🧱 Updating project"
poetry update
echo "🛠️ Updating pre-commit"
pre-commit autoupdate
echo "🎉 Successfully updated dependencies"
