"""Fill inquiry"""
from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.get('https://formsmarts.com/html-form-example')
driver.switch_to_frame(driver.find_element_by_class_name('fs_embed'))

first_name = driver.find_element_by_id('u_YOz_4607')
first_name.clear()
first_name.send_keys('Luis')

last_name = driver.find_element_by_id('u_YOz_338354')
last_name.clear()
last_name.send_keys('Rivas')

email = driver.find_element_by_id('u_YOz_4608')
email.clear()
email.send_keys('luis.rivas.0606@gmai.com')

inquiry = driver.find_element_by_id('u_YOz_4609')
inquiry.clear()
inquiry.send_keys('My Inquiry')

continue_btn = driver.find_element_by_name('submit')
continue_btn.click()
