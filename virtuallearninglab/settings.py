"""
Django settings for virtuallearninglab project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR,  "static")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

with open('secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = [
    '207.154.236.200',
    'wwww.elearning-lab.org',
    'elearning-lab.org',
    'virtual-learning-lab.herokuapp.com',
    '127.0.0.1',
    'localhost',
    'https://e-learning-lab-production.up.railway.app/',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Components.student',
    # 'Components.student.apps.StudentConfig',
    'embed_video',
    'Components.courses',
    'tinymce',
    'Components.home',
    'Components.discussion_board',
    'Components.admin_panel',
    'Components.profile',
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',
    'profanity',
    'vote',
    #quiz_app
    'Components.quiz',
    'Components.multichoice',
    'Components.true_false',
    'Components.essay',

    'Components.shoppifyPage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'virtuallearninglab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['virtuallearninglab/templates/', 'student/templates', 'zoom/templates', 'courses/templates', 'disscussion_board/templates', 'shoppifyPage/templates', os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'virtuallearninglab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

}

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

# Select Style for Crispy-Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

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
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets"),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_REDIRECT_URL = '/'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #only for testing, comment out for production
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR,  "static")
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 600,
        'width':1500,
    },
}

STRIPE_PUBLIC_KEY = 'pk_test_51NJkoBJaj77Db3vYUYmyYoMeNziW4TIpnFXPvmiXwbkt11dDNGnMhFcRTamWuu197BRJ4Es9NWA49sbeArKb52Tq00PgaWy757'
STRIPE_SECRET_KEY = 'sk_test_51NJkoBJaj77Db3vYS0aHF3TXwEulbCMZfqFdln74lc7RRgepdbOFcgLvLB9EwG7oYnjBzAIX8w4NsdaiQziadZrM0008VltKPI'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

with open('email.txt') as f:
    EMAIL_HOST_USER = f.read().strip()

with open('password.txt') as f:
    EMAIL_HOST_PASSWORD = f.read().strip()