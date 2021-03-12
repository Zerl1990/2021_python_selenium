"""Google locators"""
from selenium.webdriver.common.by import By


class GoogleLocators:
    """Google locators."""
    SEARCH_TEXT_BOX = (By.NAME, 'q')
    SEARCH_BTN = (By.NAME, 'btnK')
    FEELING_LUCKY_BTN = (By.NAME, 'btnI')
