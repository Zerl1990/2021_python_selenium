from module_05.sauce_func_lib.TestBase import TestBase
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from module_05.sauce_func_lib.inventory import get_inventory
from module_05.sauce_func_lib.login import login, get_login_error


class TestLogin(TestBase):

    _ERROR_MSG = 'Epic sadface: Username and password do not match any user in this service'

    def test_login(self):
        self.driver: WebDriver
        login(self.wait, 'standard_user', 'secret_sauce')
        items = get_inventory(self.wait)
        assert len(items) > 0, 'Inventory should be loaded'

    def test_invalid_login(self):
        login(self.wait, 'standard_user', 'invalid_secret')
        error_msg = get_login_error(self.wait)
        assert error_msg is not None, 'Error message should be displayed for invalid login'
        assert error_msg == TestBase._ERROR_MSG, f'Error message should be {TestBase._ERROR_MSG}'
        with pytest.raises(TimeoutException):
            get_inventory(self.wait)
