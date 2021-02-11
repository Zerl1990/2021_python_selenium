"""Login to facebook"""
from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.implicitly_wait(30)
driver.get('https://www.amazon.com/')
driver.find_element_by_id('invalid id')
driver.quit()
