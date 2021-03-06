"""
Django settings for aboutme project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@to4j@ygo7s617ps+e8vdj1)$*by$e-f-2q4mls2cl7a@sxy9j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_facebook',
	'usr',
	'home',
	'friends',
	'feedbacks',
	'jsonui',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aboutme.urls'

WSGI_APPLICATION = 'aboutme.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
                'read_default_file': os.path.join(BASE_DIR, 'aboutme_mysql.cnf'),
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('en-us', _('English')),
    ('pt-br', _('Brazilian Portuguese')),
    ('fr-fr', _('French')),
    ('es-es', _('Spanish')),
)

LOCALE_PATHS = (
	os.path.join(BASE_DIR, 'locales'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT='/home/luisbuen/www/aboutme/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, '_static')

TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, 'templates'),
)

#AUTH_PROFILE_MODULE = 'aboutme.UserProfile'
AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'

AUTHENTICATION_BACKENDS = (
    'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
#AUTH_USER_MODEL = 'auth.User'
#AUTH_USER_MODEL = 'aboutme.UserModel'

LOGIN_URL = '/usr/login'

# Facebook
FACEBOOK_APP_ID             = '362794893845188'
FACEBOOK_APP_SECRET         = '5d690741ca476e4d02987c82039b79bb'
FACEBOOK_PROFILE_IMAGE_PATH = os.path.join('static', 'facebook_profiles/%Y/%m/%d')

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django_facebook.context_processors.facebook',
)

