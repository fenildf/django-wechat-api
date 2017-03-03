"""
Django settings for wechat project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SAE/BAE:True means on server, False means on local.
DEPLOY = 'SERVER_SOFTWARE' in os.environ


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wfh*ff9ymrjv@v0nlfm7%pez3oi^p74d!m!o03g=ht2g#99v%m'

# SECURITY WARNING: don't run with debug turned on in production!

# SAE/BAE:on server not debug.
DEBUG = not DEPLOY

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wechat_api',
    'enterprise_api',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'wechat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'wechat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


# For SAE
if DEPLOY:
    import sae.const
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PASS = sae.const.MYSQL_PASS
    MYSQL_HOST = sae.const.MYSQL_HOST
    MYSQL_PORT = sae.const.MYSQL_PORT
# For BAE
#if DEPLOY:
#    MYSQL_DB = 'yZPwHsciFPfWvrfRnpZJ'
#    MYSQL_USER = '2ccb65f718624644a1168657a2d52958'
#    MYSQL_PASS = 'f28ab5e79d854148a7a1ae877a55e908'
#    MYSQL_HOST = 'sqld.duapp.com'
#    MYSQL_PORT = '4050'
# For Local
else:
    MYSQL_DB = 'wechat'
    MYSQL_USER = 'chengca'
    MYSQL_PASS = 'chengca'
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DB,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST,
        'PORT': MYSQL_PORT,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# For wechat subscribe and service account
WECHAT_TOKEN = "canux"
WECHAT_APP_ID = ""
WECHAT_APP_SECRET = ""

# For wechat enterprise account
CORPID = "wx2b60193d11c71526"
TOKEN = "canux"
EncodingAESKey = "6L6XDzj7GGdRSDTET6J4FMklM5FZKM8gKc76hlaplSl"
SECRET = "Ox9khNJ72tR-I6TnRLUnmdYvzIatUjruTXCD-uhjRux0sBBKCXA1XeGeJ-jF7LKy"
AGENTID = 1
SAFE = 0
