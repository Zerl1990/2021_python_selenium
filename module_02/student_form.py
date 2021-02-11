"""Fill student form."""
from selenium.webdriver.support.select import Select

from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.get('https://formsmarts.com/form/axi?mode=h5')

first_name = driver.find_element_by_id('u_GfB_60857')
first_name.clear()
first_name.send_keys('Luis')

last_name = driver.find_element_by_id('u_GfB_60858')
last_name.clear()
last_name.send_keys('Rivas')

email = driver.find_element_by_id('u_GfB_60859')
email.clear()
email.send_keys('luis.rivas.0606@gmai.com')

address = driver.find_element_by_id('u_GfB_60860')
address.clear()
address.send_keys('My Address')

country = Select(driver.find_element_by_id('u_GfB_60871'))
country.select_by_index(2)

check_in_date = driver.find_element_by_id('u_GfB_60861')
check_in_date.clear()
check_in_date.send_keys('12/12/2021')

double_room_btn = driver.find_element_by_id('u_GfB_60866_0')
double_room_btn.click()

address = driver.find_element_by_id('u_GfB_60870')
address.clear()
address.send_keys('3')

continue_btn = driver.find_element_by_name('submit')
continue_btn.click()

driver.quit()
