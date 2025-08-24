# api/index.py

# This file acts as the single entry point for Vercel.
# It imports the actual Django WSGI application.
from ananta_project.wsgi import application

# The 'app' variable is what Vercel will look for.
app = application