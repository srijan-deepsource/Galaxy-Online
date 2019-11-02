"""
Django settings for GalaxyOnline project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# imports os module. The majority of this file is automatically generated
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# designates base directory of program. Automatically generated


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uq(=53hk^d1i5e778jp8l^mr!5t#i7x-669ckjd#+h-jnt@-p('
# security key for project. automatically generated

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# sets debug value. automaticaly generated

ALLOWED_HOSTS = []
# shows allowed hosts for project. Automatically generated


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Home',
]
# this shows the installed apps that the project uses. All fields in list are automatically generated

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#this block was automatically generated by django

ROOT_URLCONF = 'GalaxyOnline.urls'
# this was automatically generated by django. it shows the root url configuration files

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
#this templates list was automatically generated by the django project

WSGI_APPLICATION = 'GalaxyOnline.wsgi.application'
# automatically generated by django project


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
#this was automatically generated by django


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
#this is the language code for the django project and was automatically generated

TIME_ZONE = 'UTC'
#this is the time zone field for the django project and was automatically generated

USE_I18N = True
# this was automatically generated by django

USE_L10N = True
# this was automatically generted by django

USE_TZ = True
# this was automatically generated by django


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# this was automatically generated by django
# this stores the static files in a static directory

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'Home/media')
# this stores the media files in a media directory

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# i added this to the file as to allow the project to locate my static folder

LOGIN_REDIRECT_URL = 'Profile'
# this redirects the user to the profile page after loggin into the system