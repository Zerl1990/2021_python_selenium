"""Explicit waits."""
from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = get_driver('chrome')
wait = WebDriverWait(driver, 10)

driver.get('https://www.youtube.com/')

search_locator = (By.ID, 'search')
search_textbox = wait.until(EC.element_to_be_clickable(search_locator))
search_textbox.send_keys('Selenium')

search_btn_locator = (By.ID, 'search-icon-legacy')
search_btn = wait.until(EC.element_to_be_clickable(search_btn_locator))
search_btn.click()

results_locator = (By.ID, 'video-title')
results = wait.until(EC.visibility_of_all_elements_located(results_locator))
print(f'Total results: {len(results)}')
for result in results:
    print(result.text)

driver.quit()
