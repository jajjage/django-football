"""
Generated by 'django-admin startproject' using Django 1.11.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from .defaults import *

# CONTEXT
PROJECT_NAME = env('PROJECT_NAME')
PROJECT_URL = env('DOMAIN')

SITE_ID = 1
INSTALLED_APPS += [
    "core",
    "users",
    "matches",
]

WEBSITE_EMAIL = DEFAULT_FROM_EMAIL
ADMIN_URL = 'admin/'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://%s.nl' % env('DOMAIN')
DEFAULT_FROM_EMAIL = 'no-reply@{}.nl'.format(env('DOMAIN'))

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/account/logout/'
LOGOUT_REDIRECT_URL = '/'

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'core.context_processors.project',
]

# WAGTAIL
# ------------------------------------------------------------------------------
# http://docs.wagtail.io/en/v2.1.1/advanced_topics/settings.html

WAGTAIL_APPS = [
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.routable_page',
    'wagtail.contrib.search_promotions',
    'wagtail.contrib.settings',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'modelcluster',
    'taggit',

    'wagtailautocomplete',
    'condensedinlinepanel',
    'wagtailmenus',
]
WAGTAIL_MIDDLEWARE = [
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]
INSTALLED_APPS = WAGTAIL_APPS + INSTALLED_APPS
MIDDLEWARE += WAGTAIL_MIDDLEWARE
WAGTAIL_SITE_NAME = env('PROJECT_SLUG')
WAGTAIL_APPEND_SLASH = True
WAGTAIL_GRAVATAR_PROVIDER_URL = None
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 20 * 1024 * 1024  # i.e. 20MB
WAGTAIL_PASSWORD_MANAGEMENT_ENABLED = True
WAGTAIL_PASSWORD_RESET_ENABLED = True
WAGTAILUSERS_PASSWORD_ENABLED = True
WAGTAILUSERS_PASSWORD_REQUIRED = True
TAGGIT_CASE_INSENSITIVE = True
WAGTAIL_AUTO_UPDATE_PREVIEW = True
WAGTAIL_USAGE_COUNT_ENABLED = True
WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = True
# WAGTAIL_USER_CUSTOM_FIELDS = ['user_type', 'logo']
TEMPLATES[0]['OPTIONS']['context_processors'].append('wagtailmenus.context_processors.wagtailmenus')
TEMPLATES[0]['OPTIONS']['context_processors'].append('wagtail.contrib.settings.context_processors.settings')


# CRISPY FORMS
# ------------------------------------------------------------------------------
# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs

INSTALLED_APPS = ['crispy_forms'] + INSTALLED_APPS
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_FAIL_SILENTLY = not DEBUG

# SORL-THUMBNAIL
# ------------------------------------------------------------------------------
# https://github.com/jazzband/sorl-thumbnail

INSTALLED_APPS += ['sorl.thumbnail']
THUMBNAIL_PRESERVE_FORMAT = True

# DJANGO-REGISTRATION-REDUX
# ------------------------------------------------------------------------------
# https://django-registration-redux.readthedocs.io/en/latest/
ACCOUNT_ACTIVATION_DAYS = 7
# should be above django.contrib.admin
INSTALLED_APPS = ['registration'] + INSTALLED_APPS

INCLUDE_AUTH_URLS = False
INCLUDE_REGISTER_URL = False # using custom View
REGISTRATION_ADMINS = ADMINS
