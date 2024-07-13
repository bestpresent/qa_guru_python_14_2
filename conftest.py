import pytest

from selene import browser


@pytest.fixture(autouse=true)
def browser_setup():
    browser.config.window_height = 2000
    browser.config.window_width = 1200
    browser.config.base_url = 'http://google.com'

    yield
    browser.quit()
