"""
Django settings for dashboard project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print "The BASE_DIR is " + BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i*&g4##t191ditltc&j7x=gni4bspt7pivr1!zz8c0c2rc^eli'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'web')]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'voting'
)

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
 'django.template.loaders.app_directories.Loader')

TEMPLATE_DIRS = (BASE_DIR + '/dashboard/templates',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dashboard.urls'

WSGI_APPLICATION = 'dashboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dashboard',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/glassteam/glassprov/dashboard/dashboard/static'
STATICFILES_DIRS = ()

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )

# WEARSCRIPT

import websocket
from wearscript.socket import websocket_client_factory,websocket_server,WebSocketClientConnection
try:
    print "os.environ['WEARSCRIPT_ENDPOINT'] is %s" % (os.environ['WEARSCRIPT_ENDPOINT'])
except KeyError:
    print "os.environ['WEARSCRIPT_ENDPOINT'] not set."
    os.environ['WEARSCRIPT_ENDPOINT'] = 'ws://glassprov.media.mit.edu:8080/ws'
client_endpoint = os.environ['WEARSCRIPT_ENDPOINT']
print "Using client_endpoint %s" % client_endpoint
# WSCONN = WebSocketClientConnection(websocket.create_connection(client_endpoint))
# WSCONN.send(
#     'glass',
#     'script',
#     {'glass.html':
#     """
#     <script>
#     WS.wake();
#     WS.activityCreate();
#     WS.displayCardTree();
#     var tree = new WS.Cards();
#     tree.add('GlassProv', '');
#     WS.cardTree(tree);
#     </script>
#     """}
# )
