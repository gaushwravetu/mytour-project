"""
Django settings for mytour project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
import dj_database_url

# DATABASES['default'] =  dj_database_url.config()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9)42))gh#1vgiun*=)sbt=zw^7l0!5*g+f5d&an!2dhu$a^u44'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dry-atoll-48133.herokuapp.com','localhost']
LOGIN_REDIRECT_URL='dashboard'


# Application definition

INSTALLED_APPS = [
    'community.apps.CommunityConfig',
    'place.apps.PlaceConfig',
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth.account',
    'allauth',
    'allauth.socialaccount',
    'ckeditor',
    'ckeditor_uploader',

    # providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

CKEDITOR_UPLOAD_PATH = '/media/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':'full'
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'mytour.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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


WSGI_APPLICATION = 'mytour.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mytour',
#         'HOST': "localhost",
#         'USER': 'postgres',
#         'PASSWORD': 'mytour@123',
#     }
# }
# DATABASE = {'default': {'NAME': 'mytour', 'USER': 'postgres', 'PASSWORD': 'mytour@123', 'HOST': 'localhost', 'PORT': '', 'CONN_MAX_AGE': 0, 'ENGINE': 'django.db.backends.postgresql_psycopg2'}}
# print(DATABASE)
#DATABASE_URL = 'postgres://postgres:mytour@123@localhost/mytour'
#DATABASES = {
#        'default': dj_database_url.parse(DATABASE_URL)
#    }
# DATABASE = {'default':dj_database_url.config(default='postgres://postgres:mytour@123@localhost/mytour')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'mytour',
        'HOST': 'localhost',
        'PORT': '',                    
        'USER': 'postgres',
        'PASSWORD': 'mytour@123',                             
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'mytour/static'),
]
# media settings added manually
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

#django message framework added manually
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

SITE_ID=6

# email settings added manually
# EMAIL_BACKEND = 'django.core.mail.backend.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'gauravmyntra097@gmail.com'
EMAIL_HOST_PASSWORD = 'Gaurav@7597604205'
EMAIL_USE_TLS = True

# whitenoise settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 
