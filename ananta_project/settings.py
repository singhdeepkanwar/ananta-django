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

# --- APPLICATION DEFINITION ---
INSTALLED_APPS = [
    'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes',
    'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles',
    'website', 'ckeditor', 'ckeditor_uploader', 'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ananta_project.urls'
TEMPLATES = [ { 'BACKEND': 'django.template.backends.django.DjangoTemplates', 'DIRS': [os.path.join(BASE_DIR, 'templates')], 'APP_DIRS': True, 'OPTIONS': { 'context_processors': [ 'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth', 'django.contrib.messages.context_processors.messages', ], }, }, ]

# --- DATABASE CONFIGURATION ---
DATABASES = { 'default': dj_database_url.config(default=f'sqlite:///{BASE_DIR / "db.sqlite3"}', conn_max_age=600, ssl_require=False) }

# --- OTHER CORE SETTINGS ---
AUTH_PASSWORD_VALIDATORS = [ {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}, {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'}, {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'}, {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}, ]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- STATIC & MEDIA FILES (FINAL CONFIGURATION) ---

# This is the official way to detect if the code is running on Vercel
IS_PRODUCTION = os.environ.get('VERCEL') == '1'

# Static Files (CSS, JavaScript)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

if IS_PRODUCTION:
    # --- PRODUCTION SETTINGS (Vercel & Supabase) ---
    
    # Supabase Storage Credentials
    AWS_ACCESS_KEY_ID = os.environ.get('SUPABASE_PROJECT_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('SUPABASE_SERVICE_KEY')
    AWS_STORAGE_BUCKET_NAME = 'ananta-storage' # Use your lowercase bucket name
    
    # This is the crucial part for Supabase to work with boto3
    AWS_S3_ENDPOINT_URL = f"https://{os.environ.get('SUPABASE_PROJECT_ID')}.supabase.co/storage/v1/s3"
    
    # This generates the correct public URLs for your files
    AWS_S3_CUSTOM_DOMAIN = f"{os.environ.get('SUPABASE_PROJECT_ID')}.supabase.co/storage/v1/s3/object/public/{AWS_STORAGE_BUCKET_NAME}"
    
    # Other necessary settings for Supabase compatibility
    AWS_S3_OBJECT_PARAMETERS = { 'CacheControl': 'max-age=86400', }
    AWS_DEFAULT_ACL = 'public-read'
    AWS_LOCATION = '' # This MUST be an empty string for Supabase
    AWS_QUERYSTRING_AUTH = False # Disable signed URLs for public files

    # The modern STORAGES dictionary for Django 4.2+
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
else:
    # --- LOCAL DEVELOPMENT SETTINGS ---
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    
    # Use local file system for media in development
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }

# --- OTHER APP SETTINGS ---
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@anantagroup.com'

# Tell CKEditor to use the default storage backend (which will be S3 in production)
CKEDITOR_STORAGE_BACKEND = 'django.core.files.storage.get_storage_class'
CKEDITOR_UPLOAD_PATH = "uploads/"