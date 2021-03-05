"""Includes function to control sauce lab login page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from module_05.sauce_func_lib.common import write_to_input, click


def login(wait: WebDriverWait, user: str, password: str):
    """Login to sauce lab.

    :param wait: Instance of web driver wait.
    :param user: User email
    :param password: USer password
    :return: None
    """
    write_to_input(wait, (By.ID, 'user-name'), user)
    write_to_input(wait, (By.ID, 'password'), password)
    click(wait, (By.ID, 'login-button'))
