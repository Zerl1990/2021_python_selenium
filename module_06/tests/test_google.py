"""Test google."""
from common.webdriver_factory import get_driver
from module_06.src.pages.google import Google


def test_google_search():
    driver = get_driver('chrome')
    page = Google(driver)
    page.open()
    page.search('Selenium')


def test_feeling_lucky():
    driver = get_driver('chrome')
    page = Google(driver)
    page.open()
    page.feeling_lucky('Selenium')
