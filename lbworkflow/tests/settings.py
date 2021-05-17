"""
Django settings for testproject project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "*lx!g2o%m)b613n$709334=+ulwi^&6e8=o6h3upwn4&3c$o^p"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "lbattachment",
    "lbadminlte",
    "lbutils",
    "compressor",
    "djangobower",
    "django_select2",
    "bootstrap_pagination",
    "lbworkflow",
    "lbworkflow.simplewf",
    "lbworkflow.tests.leave",
    "lbworkflow.tests.purchase",
    "lbworkflow.tests.issue",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lbworkflow.tests.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "testproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = "/static/"

LBWF_APPS = {
    "leave": "lbworkflow.tests.leave",
    "purchase": "lbworkflow.tests.purchase",
    "simplewf": "lbworkflow.simplewf",
}

STATIC_ROOT = os.path.join(BASE_DIR, "collectedstatic")

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

CRISPY_TEMPLATE_PACK = "bootstrap3"

# bower
STATICFILES_FINDERS += (("djangobower.finders.BowerFinder"),)
BOWER_COMPONENTS_ROOT = BASE_DIR

BOWER_INSTALLED_APPS = (
    "admin-lte#2.3.11",
    "font-awesome#4.7.0",
    "ionicons#2.0.1",
    "modernizr",
    # POLYFILLS: javascript fallback solutions for older browsers.
    # CSS3 selectors for IE 6-8.
    "selectivizr",
    # min/max width media queries for IE 6-8.
    "respond",
    # CSS3 styles for IE 6-8.
    "pie",
    # HTML5 tag support for IE 6-8.
    "html5shiv",
    "masonry#4.1.1",
    "blueimp-file-upload#9.12.5",
    "flatpickr-calendar#2.5.6",
)

# django-compressor
STATICFILES_FINDERS += (("compressor.finders.CompressorFinder"),)
COMPRESS_PRECOMPILERS = (
    ("text/coffeescript", "coffee --compile --stdio"),
    ("text/less", "lessc {infile} {outfile}"),
    ("text/x-sass", "sass {infile} {outfile}"),
    ("text/x-scss", "sass --scss {infile} {outfile}"),
)

PROJECT_TITLE = "LB-Workflow"

LBWF_DEFAULT_PERMISSION_CLASSES = ["lbworkflow.views.permissions.AllowAny"]
LBWF_DEFAULT_NEW_PERMISSION_CLASSES = [
    "lbworkflow.tests.permissions.TestPermission"
]
# LBWF_DEFAULT_EDIT_PERMISSION_CLASSES = ['lbworkflow.views.permissions.AllowAny']
