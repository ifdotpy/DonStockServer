"""
Django settings for DonStockServer project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9=ya6d9mb70y1zf^6fh$($2i&n-vv^43t!a^*0xgs2#iwb(x+@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework',
	'REST',
	'oauth2_provider',
	'social_django',
	'rest_framework_social_oauth2',
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

ROOT_URLCONF = 'DonStockServer.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')]
		,
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'social_django.context_processors.backends',
				'social_django.context_processors.login_redirect',
			],
		},
	},
]

WSGI_APPLICATION = 'DonStockServer.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
		'rest_framework_social_oauth2.authentication.SocialAuthentication',
	),
}

AUTHENTICATION_BACKENDS = (
	# Facebook OAuth2
	'social_core.backends.facebook.FacebookAppOAuth2',
	'social_core.backends.facebook.FacebookOAuth2',
	# VK OAuth2
	'social_core.backends.vk.VKOAuth2',
	# GooglePlus OAuth2
	'social_core.backends.google.GooglePlusAuth',
	# Other Stuff
	'rest_framework_social_oauth2.backends.DjangoOAuth2',
	'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_VK_OAUTH2_KEY = '6331649'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'xU60LE2ww7hGuy7fURck'

SOCIAL_AUTH_GOOGLE_PLUS_KEY = '144970166473-2s4duvd0q88q1apm43k7fkvlr7ips0i7.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = '9QmUjsKeCpVD0GYW4PwhpUoG'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'   # здесь мог бы быть ваш редирект
SOCIAL_AUTH_GOOGLE_OAUTH2_USE_UNIQUE_USER_ID = True


SOCIAL_AUTH_FACEBOOK_KEY = '1887275517980140'
SOCIAL_AUTH_FACEBOOK_SECRET = 'l1CBSDO8t8o3ho1qxJaBygMD5ys'


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
