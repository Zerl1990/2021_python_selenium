"""Test cases for login"""
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver
from module_05.sauce_func_lib.inventory import get_inventory
from module_05.sauce_func_lib.login import login


LOGIN_DATA = [
    ('standard_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
]


@pytest.mark.parametrize('user, password', LOGIN_DATA)
def test_valid_user(user: str, password: str):
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')
    items = get_inventory(wait)
    assert len(items) > 0, 'Inventory should be loaded'
    driver.close()


def test_invalid_user():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'invalid_secret')
    with pytest.raises(TimeoutException):
        get_inventory(wait)
    driver.close()


