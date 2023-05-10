import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    def select_option_by_text(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)

    def clear_and_enter(self, locator, text):
        locator.clear()
        locator.send_keys(text)