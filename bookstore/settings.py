"""
Django's settings for bookstore project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '#_&=00i)tksdb#v5+5_bo=e8--m@1awp(k=q%1lv+fepvve%z)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG = True //For localhost development

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = [
    'https://recbookstore.azurewebsites.net',
    'localhost',
    '127.0.0.1'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'about.apps.AboutConfig',
    'accounts.apps.AccountsConfig',
    'contact.apps.ContactConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookstore.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookstore.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'bookstore',
#         'USER': 'varun',
#         'PASSWORD': 'OneTwoThree4',
#         'SERVER': 'konoserver.database.windows.net',
#         'PORT': '1433'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.environ.get('DBNAME'),
        'USER': os.environ.get('DBUSER'),
        'PASSWORD': os.environ.get('DBPASS'),
        'Trusted_Connection': 'no',
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT'),
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
            'extra_params': "Encrypt=yes;TrustServerCertificate=no",
        },
    },
}
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

DEFAULT_FILE_STORAGE = 'core.azure_storage.AzureMediaStorage'
STATICFILES_STORAGE = 'core.azure_storage.AzureStaticStorage'

AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
#
# # Deployment
# # Directory where collectstatic will collect the static files for deployment
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
#
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# MEDIA_URL = "/media/"

LOGIN_REDIRECT_URL = "shop:base"
LOGOUT_REDIRECT_URL = "shop:base"

CART_SESSION_ID = 'cart'

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

PRODUCTS_PER_PAGE = 12

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'example@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587
