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
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # This is essential
    'website',
    'ckeditor',
    'ckeditor_uploader',
]

# --- MIDDLEWARE (NO WHITENOISE) ---
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
        'OPTIONS': { 'context_processors': [ 'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth', 'django.contrib.messages.context_processors.messages', ], },
    },
]

# --- DATABASE CONFIGURATION ---
DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3', } }
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.config(default=DATABASE_URL, conn_max_age=600, ssl_require=False)

# --- PASSWORD VALIDATION ---
AUTH_PASSWORD_VALIDATORS = [ {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}, {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'}, {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'}, {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}, ]

# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- STATIC & MEDIA FILES (Configured for Vercel Native Serving) ---
STATIC_URL = '/static/'
# This is where Django will look for your source static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# This is the single output directory where 'collectstatic' will place ALL static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- OTHER SETTINGS ---
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@anantagroup.com'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = { 'default': { 'toolbar': 'full', 'height': 300, 'width': '100%'}, }