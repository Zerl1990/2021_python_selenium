"""Google search page."""
from selenium.webdriver.remote.webdriver import WebDriver
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators.google import GoogleLocators
from module_06.src.pages.base_page import BasePage


_URL = 'https://www.google.com/'


class Google(BasePage):
    """Google base page."""

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.__search_textbox = BasePageElement(GoogleLocators.SEARCH_TEXT_BOX, wait=self._wait)
        self.__search_btn = BasePageElement(GoogleLocators.SEARCH_BTN, wait=self._wait)
        self.__feeling_lucky_btn = BasePageElement(GoogleLocators.FEELING_LUCKY_BTN, wait=self._wait)

    def search(self, value):
        """Simple search."""
        self.__search_textbox.write(value)
        self.__search_btn.click()

    def feeling_lucky(self, value):
        """Feeling lucky search."""
        self.__search_textbox.write(value)
        self.__feeling_lucky_btn.click()


