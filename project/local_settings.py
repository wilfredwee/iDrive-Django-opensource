import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db.sqlite35',                      # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# if not DEBUG:
#     DATABASES = {
#         'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': os.environ['RDS_DB_NAME'],
#         'USER': os.environ['RDS_USERNAME'],
#         'PASSWORD': os.environ['RDS_PASSWORD'],
#         'HOST': os.environ['RDS_HOSTNAME'],
#         'PORT': os.environ['RDS_PORT'],
#         }
#     }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Vancouver'

# Absolute filesystem path to the directory that will hold user-uploaded files.

# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
if DEBUG:
    STATIC_URL = '/static/'
else:
    STATIC_URL = 'https://s3-us-west-2.amazonaws.com/elasticbeanstalk-us-west-2-266817843873/static/'

    STATIC_ROOT = os.path.join(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__))), 'static')

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_ACCESS_KEY_ID = 'key_here'
    AWS_SECRET_ACCESS_KEY = 'key_here'
    AWS_STORAGE_BUCKET_NAME = 'bucket_name_here'

# Additional locations of static files
# STATICFILES_DIRS = (
#     # Put strings here, like "/home/html/static" or "C:/www/django/static".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
# )

PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__name__)), 'project/')
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "static"),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'key_here'

DEBUG_APPS = ()
