"""Test implementation of base page element."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver
from module_06.lib.elements.base_page_element import BasePageElement


def test_page_without_root():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.google.com/')
    locator = (By.NAME, 'q')
    element = BasePageElement(locator, wait=wait)
    element.write('Selenium')
    assert element.get_value() == 'Selenium'
    driver.quit()


def test_base_page_with_root():
    driver = get_driver('chrome')
    driver.get('https://www.google.com/')
    root_element = driver.find_element_by_class_name('SDkEP')
    locator = (By.NAME, 'q')
    element = BasePageElement(locator, root=root_element)
    element.write('Selenium')
    assert element.get_value() == 'Selenium'
    driver.quit()



