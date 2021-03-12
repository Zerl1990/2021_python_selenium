"""Sauce lab login tests."""
from common.webdriver_factory import get_driver
from module_06.src.pages.sauce_lab_login import SauceLabLogin


def test_sauce_lab_login():
    driver = get_driver('chrome')
    page = SauceLabLogin(driver)
    page.open()
    page.login('standard_user', 'secret_sauce')
    driver.quit()
