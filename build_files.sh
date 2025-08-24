#!/bin/bash

# Exit on error
set -e

echo "Building project..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations (if using a persistent database)
# For Vercel's ephemeral filesystem with SQLite, this runs on each deploy.
python manage.py migrate

echo "Build finished."