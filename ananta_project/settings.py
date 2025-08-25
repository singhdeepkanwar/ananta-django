# ananta_project/settings.py

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

# --- CORE SETTINGS ---
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

WSGI_APPLICATION = 'ananta_project.wsgi.application'

ALLOWED_HOSTS = []
SITE_URL = os.environ.get('SITE_URL')
if SITE_URL:
    ALLOWED_HOSTS.append(SITE_URL)
if DEBUG:
    ALLOWED_HOSTS.append('127.0.0.1')


# --- APPLICATION DEFINITION ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'ckeditor',
    'ckeditor_uploader',
]

# --- MIDDLEWARE (No Whitenoise) ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ananta_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- DATABASE CONFIGURATION ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.config(default=DATABASE_URL, conn_max_age=600, ssl_require=False)

# --- PASSWORD VALIDATION ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- STATIC & MEDIA FILES (Configured for Vercel & Supabase Storage) ---

IS_PRODUCTION = os.environ.get('VERCEL') == '1'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

# Define Media files settings globally
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Use the cloud storage backend ONLY in production
if IS_PRODUCTION:
    # Use the custom storage class we created in ananta_project/storages.py
    DEFAULT_FILE_STORAGE = 'ananta_project.storages.MediaStorage'
    
    # Supabase/S3 credentials
    AWS_ACCESS_KEY_ID = os.environ.get('SUPABASE_PROJECT_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('SUPABASE_SERVICE_KEY')
    AWS_STORAGE_BUCKET_NAME = 'AnantaStorage'
    AWS_S3_ENDPOINT_URL = os.environ.get('SUPABASE_S3_ENDPOINT_URL')
    
    # These settings are important for generating correct public URLs
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_ACCESS_KEY_ID}.supabase.co/storage/v1/object/public/{AWS_STORAGE_BUCKET_NAME}'
    AWS_LOCATION = ''
    AWS_QUERYSTRING_AUTH = False # Important for public files
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = 'public-read'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- OTHER SETTINGS ---
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@anantagroup.com'

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': { 'toolbar': 'full', 'height': 300, 'width': '100%'},
}