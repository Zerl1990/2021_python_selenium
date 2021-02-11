"""Web Driver Example"""
from common.webdriver_factory import get_driver

driver = get_driver('firefox')
driver.get('https://google.com')
gmail_link = driver.find_element_by_link_text('Gmail')
print(f'Gmail link is displayed: {gmail_link.is_displayed()}')
print(f'Gmail link is enabled: {gmail_link.is_enabled()}')
print(f'Gmail link is selected: {gmail_link.is_selected()}')
if gmail_link.is_enabled() and gmail_link.is_displayed():
    gmail_link.click()

driver.quit()
