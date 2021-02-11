"""Login to facebook"""
from common.webdriver_factory import get_driver
from selenium.webdriver.support.ui import Select


driver = get_driver('chrome')
driver.get('https://www.amazon.com/')

element = driver.find_element_by_id('searchDropdownBox')
dropdown = Select(element)

print(f'Is multiple selection enabled: {dropdown.is_multiple}')

dropdown.select_by_visible_text('Deals')
print(f'Current selection: {dropdown.first_selected_option.text}')

dropdown.select_by_visible_text('Books')
print(f'Current selection: {dropdown.first_selected_option.text}')

driver.quit()
