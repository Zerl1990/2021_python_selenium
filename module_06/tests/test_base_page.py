"""Test implementation of base page."""
from common.webdriver_factory import get_driver
from module_06.src.pages.base_page import BasePage


def test_base_page():
    driver = get_driver('chrome')
    page = BasePage(driver, 'https://www.google.com/')
    page.open()
    page.wait_until_loaded()
    page.timeout = 5
    assert page.timeout == 5, 'Page timeout should be 5'
    page.close()


