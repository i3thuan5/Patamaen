from .settings import *  # noqa
from .settings import INSTALLED_APPS

ALLOWED_HOSTS = [
    # for docker selenium
    'rime-gunicorn',
]

INSTALLED_APPS += [
    'behave_django',
]

STATIC_ROOT = '/staticfiles/'
