"""Django settings for quackdownproject project.

This file contains all the development settings.
Production settings are imported at the end of this file and override these
settings where necessary. If the production settings file is not available,
then importing it fails silently. The production settings file is not in the
repository because it contains the SECRET_KEY.
"""
import os

QUACKDOWN_VERSION = "0.2beta"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Nathan Geffen', 'nathan@tac.org.za'),
)

SERVER_EMAIL = 'nathan@tac.org.za'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'quackdown.sqlite'),
    'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Johannesburg'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/nathan/programming/django-quackdown/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'quackdownproject.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'filebrowser',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.databrowse',
    'django.contrib.comments',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'profiles',
    'sorl.thumbnail',
    'tagging',
    'registration',
    'contact_form',
    'stopspam',
    'haystack',
    'treemenus',
    'pubman',
    'siteconfig',
    'quackdown',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "pubman.context_processors.settings",
    "pubman.context_processors.featured_content",
    "siteconfig.context_processors.rootdivision",
)

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

#TEMPLATE_DIRS = (
#    os.path.join(SITE_ROOT, 'templates'),)

HAYSTACK_SITECONF = 'pubman.search_sites'
HAYSTACK_SEARCH_ENGINE = 'xapian'
HAYSTACK_XAPIAN_PATH = os.path.join(SITE_ROOT, 'xapian/site_index')
#HAYSTACK_WHOOSH_PATH = os.path.join(SITE_ROOT, 'whoosh')

# This is the development environment secret key only.
SECRET_KEY = 'abcde'


ACCOUNT_ACTIVATION_DAYS = 2 # This is 2 days. You can change this.
LOGIN_REDIRECT_URL = '/' # This is a default. You can change this.
AUTHENTICATION_BACKENDS = (
    'pubman.accounts.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)
AUTH_PROFILE_MODULE = 'pubman.UserProfile'

if DEBUG==True:
    CACHE_BACKEND = 'dummy://'
else:
    CACHE_BACKEND = 'memcached://www.example.com:11211/'


# Pubman settings

GRAPPELLI_ADMIN_TITLE = "Quackdown Administration"

STATIC_ROOT = os.path.join(SITE_ROOT, "static/")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

# Additional locations of static files
STATICFILES_DIRS = (
    '/home/nathan/programming/myvirtualenv/lib/python2.6/site-packages/filebrowser/media',
    '/home/nathan/programming/django-pubman/pubman/media',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



#FILEBROWSER settings

FILEBROWSER_DIRECTORY = ''

FILEBROWSER_URL_FILEBROWSER_MEDIA = STATIC_URL + "filebrowser/"
FILEBROWSER_PATH_FILEBROWSER_MEDIA = STATIC_ROOT + 'filebrowser/'
#FILEBROWSER_URL_TINYMCE = STATIC_URL + "grappelli/tinymce/"
#FILEBROWSER_PATH_TINYMCE = STATIC_ROOT + 'grappelli/tinymce/'



PUBMAN_EMAIL_COMMENTS_TO_STAFF = True
PUBMAN_COMMENTS_MODERATED = True
PUBMAN_MODERATION_FREE_DAYS = 14


PUBMAN_URLCONF_VIEWS = ('search',
                   'rss',
                   'atom',
                   'i18n',
                   'accounts',
                   'comments',
                   'contact',
                   'profiles',
                   'sitemap',)

try:
    from settings_development import *
except ImportError:
    pass


try:
    from settings_production import *
except ImportError:
    pass
