"""
Django settings for disasterinfosite project.
"""

ADMINS = (
          ('Melinda Minch', 'melinda@melindaminch.com')
         )

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os import environ
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY_SEATTLE']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '10.0.2.2']
else:
    # hazardready.org is the current production server. 23.92.25.126 is its numeric address. eldang.eldan.co.uk is our demo/test server
    ALLOWED_HOSTS = ['.hazardready.org', '23.92.25.126']

# Application definition
INSTALLED_APPS = (
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'embed_video',
    'disasterinfosite',
    'solo',
    'webpack_loader'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'disasterinfosite.urls'

WSGI_APPLICATION = 'disasterinfosite.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
LANGUAGE_CODE = 'en'
USE_L10N = True

# Somali is not an officially supported language in Django, so this is a patch to add it.
import django.conf.locale
django.conf.locale.LANG_INFO['so'] = {
    'bidi': False,
    'code': 'so',
    'name': 'Somali',
    'name_local': u'af Soomaali',
}

# Add an alias for Chinese = cn, as well, for neatness. This is the same as simplified Chinese.
django.conf.locale.LANG_INFO['cn'] = {
    'bidi': False,
    'code': 'cn',
    'name': 'Chinese',
    'name_local': '简体中文',
}

gettext = lambda s: s
LANGUAGES = (
    ('cn', gettext('Chinese')),
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
    ('so', gettext('Somali')),
    ('es', gettext('Spanish')),
    ('vi', gettext('Vietnamese'))
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

USE_I18N = True
TIME_ZONE = 'UTC'
USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
            # Template caching is on by default in 1.11, so take this out on upgrade.
                ('django.template.loaders.cached.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',)
                )
            ]
        },
    },
]


### HEROKU CONFIGURATIONS ###
# Added per instructions at https://devcenter.heroku.com/articles/getting-started-with-django

# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES = {}
DATABASES['default'] =  dj_database_url.parse(os.environ["DATABASE_URL_SEATTLE"])
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# Allow database connections to persist
CONN_MAX_AGE = environ.get('CONN_MAX_AGE') or 0

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static asset configuration
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'build/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.map']
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'media')

# Use this setting if the app is being served at the domain root (e.g. hazardready.org/ )
STATIC_URL = '/seattle/static/'

# If the app is being served in a subdirectory of the domain (e.g. foo.com/SUBDIR/ ) then use a variant of:
# STATIC_URL = '/SUBDIR/static/'
# So for our current test server, eldang.eldan.co.uk/zr/ , we need:
# STATIC_URL = '/zr/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Specially for GeoDjango on Heroku
GEOS_LIBRARY_PATH = environ.get('GEOS_LIBRARY_PATH')
GDAL_LIBRARY_PATH = environ.get('GDAL_LIBRARY_PATH')

### ^^^^^^^^^^^^^^^^^^^^^^^^^ ###
### END HEROKU CONFIGURATIONS ###

MEDIA_ROOT = os.path.join(BASE_DIR, 'media', 'img')
MEDIA_URL = '/seattle/static/img/'
