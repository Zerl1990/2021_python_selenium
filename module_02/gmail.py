"""Navigate selenium page."""
from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.implicitly_wait(5)
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&dsh=S-754881558%3A1613063574131574&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')

first_name = driver.find_element_by_id('firstName')
first_name.clear()
first_name.send_keys('Luis')

first_name = driver.find_element_by_id('lastName')
first_name.clear()
first_name.send_keys('Rivas')

first_name = driver.find_element_by_id('username')
first_name.clear()
first_name.send_keys('qa_minds')

first_name = driver.find_element_by_name('Passwd')
first_name.clear()
first_name.send_keys('MyPass')

first_name = driver.find_element_by_name('ConfirmPasswd')
first_name.clear()
first_name.send_keys('MyPass')

driver.quit()