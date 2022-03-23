from .settings import *  # noqa
from .settings import INSTALLED_APPS

INSTALLED_APPS += [
    'behave_django',
]

STATIC_ROOT = '/staticfiles/'
STATIC_URL = '/static/'
