"""Explicit waits."""
import time
from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def print_decorator(func):
    """Decorator to print when function is called"""
    def _wrapper(*args):
        print(f'Calling find elements: {args}')
        return func(*args)
    return _wrapper


driver = get_driver('chrome')

# NOT RECOMMENDED!!!
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 20)

# Monkey Patch Find element
driver.find_element = print_decorator(driver.find_element)

driver.get('https://www.amazon.com/')


locator = (By.ID, 'invalid_id')

start = time.time()
try:
    search_textbox = wait.until(EC.visibility_of_element_located(locator))
except Exception:
    pass
finally:
    print(f'Total wait time: {time.time() - start}')

driver.quit()
