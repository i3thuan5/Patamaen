from behave import use_fixture
from behave.fixture import fixture
import behave_webdriver
# from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings
from django.core.management import call_command
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from unittest.mock import patch


def before_all(context):
    use_fixture(browser_chrome, context, timeout=10)
    # Kā django docker khui--khui
    # StaticLiveServerTestCase.host = '0.0.0.0'
    settings.STATIC_URL = '/static/'


def django_ready(context, *args):
    # Hōo selenium docker liân-lâi āu-tâi (nginx tī kāng-khuán docker network)
    context.tsuki = context.test.live_server_url
    # .replace(
    #     '0.0.0.0', 'patamaen-django'
    # )


def after_step(context, step):
    context.browser.get_screenshot_as_file(
        '/behave_steps/{}.png'.format(step)
    )


@fixture
def browser_chrome(context, timeout=30, **kwargs):
    # -- SETUP-FIXTURE PART:
    context.browser = behave_webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )
    context.browser.implicitly_wait(3)
    yield
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()
