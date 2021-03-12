"""Implements sauce lab login abstraction."""
from selenium.webdriver.remote.webdriver import WebDriver
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators.sauce_lab_login import SauceLabLoginLocators
from module_06.src.pages.base_page import BasePage


_URL = 'https://www.saucedemo.com/'


class SauceLabLogin(BasePage):
    """Sauce lab login."""

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.__user = BasePageElement(SauceLabLoginLocators.USER, wait=self._wait)
        self.__password = BasePageElement(SauceLabLoginLocators.PASSWORD, wait=self._wait)
        self.__login = BasePageElement(SauceLabLoginLocators.LOGIN, wait=self._wait)

    def login(self, user, password):
        """Login to sauce lab"""
        self.__user.write(user)
        self.__password.write(password)
        self.__login.click()
