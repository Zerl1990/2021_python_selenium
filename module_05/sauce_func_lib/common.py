"""Common functions."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def write_to_input(wait: WebDriverWait, locator: By, value: str):
    """Clear and write to input field.

    :param wait: Instance of web driver wait.
    :param locator: ---
    :param value: Value to write
    :return:
    """
    element = wait.until(EC.element_to_be_clickable(locator))
    element.clear()
    element.send_keys(value)


def click(wait: WebDriverWait, locator: By):
    """Wait until element is clickable and click.

    :param wait: Instance of web driver wait.
    :param locator: ----
    :return:
    """
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()
