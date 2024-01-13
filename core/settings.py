"""
Django settings for core project.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os
import environ

import pymysql

pymysql.install_as_MySQLdb()

# Read the .env file
env = environ.Env()
environ.Env.read_env()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Simplified BASE_URL_FE and BASE_URL_BE based on DEBUG value
BASE_URL_FE = 'http://localhost:3000/' if env('DEBUG') else 'https://onedreamproperty.com.my'
BASE_URL_BE = 'http://127.0.0.1:8000/' if env('DEBUG') else 'https://onedream.dynamicdigital.guru'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mm3a((@)#f%sbqjedxgcwta=^1r%)dsql131es!)l7o7ockmku'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['onedream.dynamicdigital.guru',
                 'localhost', '127.0.0.1', 'agent.tripleonestudio.com' , 'django.tripleonestudio.com' ]


# Application definition

INSTALLED_APPS = [
    # 'admin_reorder',
    'location_field.apps.DefaultConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'teams',
    'branchs',
    'users',
    'profiles',
    'blog',
    'blog_api',
    'inventory',
    'inventory_api',

    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'import_export',
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # 'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

LOCATION_FIELD_PATH = '/static/location_field'

LOCATION_FIELD = {
    'search.provider': 'google',
    'map.provider': 'mapbox',
    
    'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    'provider.google.api_key': 'AIzaSyCw3wsa90tFvFey2uNhqaA3iIn_eLCFTv8',
    'provider.google.api_libraries': '',
    'provider.google.map.type': 'ROADMAP',
    'provider.google.max_zoom': 18,
    
    
    'provider.mapbox.access_token': 'pk.eyJ1Ijoib25lZHJlYW1wcm9wZXJ0eSIsImEiOiJjbHE0bWhoM2kwN3lsMnFuNmQzYjFxbnI1In0.AVeStt8G9RI8vdfeChun1w',
    'provider.mapbox.max_zoom': 18,
    'provider.mapbox.id': 'mapbox.streets',
    
    
    
    # misc
    'resources.root_path': LOCATION_FIELD_PATH,
    'resources.media': {
        'js': (
            LOCATION_FIELD_PATH + '/js/form.js',
        ),
    },
}


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kuala_Lumpur'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Static Root masa kat production, masa run collectstatic ni kena on
# STATIC_ROOT = os.path.join(BASE_DIR, 'globalstaticfiles')

# staticfiles kat development, masa run collectstatic ni kena off
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'globalstaticfiles'),
)

# global staticfiles kat production
#STATICFILES_DIRS = (
#  os.path.join(BASE_DIR, 'globalstaticfiles'),
#)

# Absolute filesystem path to the directory that will hold static files at production, can test when debug is False
#STATIC_ROOT = BASE_DIR / "staticfiles"

#folder name for static asset kat development, dia akan pakai bila debug set as true
STATIC_URL = '/static/'

IMPORT_EXPORT_USE_TRANSACTIONS = False

# Media Settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




# REST Framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 250,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

}

FILTERS_DEFAULT_LOOKUP_EXPR = 'icontains'
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    "https://onedreamproperty.com.my",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

# custom user model
AUTH_USER_MODEL = "users.NewUser"

# Simple JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('JWT', 'Bearer'),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# EMAIL_HOST = 'smtp.mailtrap.io'
# EMAIL_HOST_USER = '8edf0ecc091b47'
# EMAIL_HOST_PASSWORD = 'c580fcfe6bd172'
# EMAIL_PORT = '2525'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'web.onedreamproperty@gmail.com'
EMAIL_HOST_PASSWORD = 'lxtbmjcetynjubjj'


# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = 5242880
FILE_UPLOAD_MAX_MEMORY_SIZE = 20971520
DATA_UPLOAD_MAX_MEMORY = 104857600

# import django_heroku
# django_heroku.settings(locals())


# ADMIN_REORDER = (
#     # Reorder app models  
#     {
#         'app': 'auth',
#         'label': 'List Unit',
#         'models': (
#             {'model': 'inventory.Inventory' ,'label' : 'All Listing' },
#             {'model': 'inventory.Category' ,'label' : 'Category' },
#             {'model': 'inventory.PropertyType' ,'label' : 'Property Type' },
#     )},
        
#     {'app': 'auth','label': 'User', 'models': (
        
#         {'model': 'branchs.Branch' ,'label' : 'Branch' },
#         {'model': 'teams.Team' ,'label' : 'Team' },
#         {'model': 'users.NewUser' ,'label' : 'Agent' }, 
#         # {'model': 'inventory.Inventory' ,'label' : 'Inventory' }
    
#       )},
# )