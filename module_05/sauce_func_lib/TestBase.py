"""Base test class"""
from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver


class TestBase:
    """Test Base"""

    def setup_method(self):
        """Setup method"""
        print('Method setup')
        self.driver = get_driver('chrome')
        self.wait = WebDriverWait(self.driver, 3)
        self.driver.get('https://www.saucedemo.com/')

    def teardown_method(self):
        """Teardown method"""
        print('Method teardown')
        if self.driver:
            self.driver.close()
