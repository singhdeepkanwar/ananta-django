#!/bin/bash

# Exit on error
set -e

echo "Building project..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
# This command finds ALL static files (yours and the admin's)
# and copies them to the STATIC_ROOT directory ('staticfiles_build/static').
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

echo "Build finished."