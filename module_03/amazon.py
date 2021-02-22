"""Run xpath in Amazon."""
from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.implicitly_wait(10)
driver.get('https://www.amazon.com.mx/')

print('A elements:')
a_lst = driver.find_elements_by_xpath("//a")
print(f'Total Elements: {len(a_lst)}')
for element in a_lst:
    print(f'{element.text} - {element.get_attribute("href")}')

print('Head children:')
head_children = driver.find_elements_by_xpath("//head/*")
print(f'Total Elements: {len(head_children)}')
for element in head_children:
    print(element.get_attribute("href"))

driver.quit()
