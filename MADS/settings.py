"""
Django settings for MADS project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import environ
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j36x(4o#*@f6aujcr*g^^o1j*0760bxf)_47ok_&*$nx@_&09('

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
env = environ.Env( DEBUG=(bool, False) )
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS=["*"]
AUTH_USER_MODEL = 'accounts.CustomUser'

# Application definition

INSTALLED_APPS = [
    'base.apps.BaseConfig',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MADS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MADS.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME', default='void'),
        'HOST': env('DB_HOST', default='void'),
        'USER': env('DB_USER', default='void'),
        'PASSWORD': env('DB_PASS', default='void'),
        'PORT': env.int('DB_PORT', default=5432)
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
DATETIME_INPUT_FORMATS = ['%d/%m/%y %H:%M:%S.%f']

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# https://stackoverflow.com/questions/24022558/differences-between-staticfiles-dir-static-root-and-media-root
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
else:
    # STATIC_ROOT = '/home/django/www-data/site.com/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # where django should save the files
# MEDIA_URL = '/media/'  # at what address you want to find the media files

AUTH_USER_MODEL = 'accounts.CustomUser'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# :: Email settings :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
SMTP_SERVER = env.bool('SMTP_SERVER', default=False)
if SMTP_SERVER:
    # Gmail SMTP server
    EMAIL_BACKEND = env('EMAIL_BACKEND', default='void')
    EMAIL_HOST = env('EMAIL_HOST', default='void')
    EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default='False')
    EMAIL_PORT = env.int('EMAIL_PORT', default='999')
    EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='void')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='void')
    DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='void')
else:
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

# :: Messages settings ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
ERROR_MESSAGE = 'Se presentó un error inesperado, por favor informar al administrador'
PERMISSION_MESSAGE = 'Ups! al parecer no tienes los permisos requeridos para acceder a esta sección'
REQUIRED_LOGIN_MESSAGE = 'Debes iniciar sesión para acceder a esta sección'

MESSAGE_TAGS = {
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}