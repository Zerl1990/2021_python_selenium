"""Explicit waits."""
from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = get_driver('chrome')
wait = WebDriverWait(driver, 5)

driver.get('https://www.amazon.com/')

locator = (By.ID, 'twotabsearchtextbox')
search_textbox = wait.until(EC.visibility_of_element_located(locator))

search_textbox.clear()
search_textbox.send_keys('Selenium')

driver.quit()
