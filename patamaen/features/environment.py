from behave import use_fixture
from behave.fixture import fixture
import behave_webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_all(context):
    use_fixture(browser_chrome, context, timeout=10)


def after_step(context, step):
    context.browser.get_screenshot_as_file(
        'behave_steps/{}.png'.format(step)
    )


@fixture
def browser_chrome(context, timeout=30, **kwargs):
    # -- SETUP-FIXTURE PART:
    context.browser = behave_webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )
    context.browser.implicitly_wait(30)
    yield
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()
