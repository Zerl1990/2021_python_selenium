"""Search in tiktok"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def search(wait: WebDriverWait, value: str):
    """Search in pinterest."""
    textbox_locator = (By.NAME, "q")
    textbox = wait.until(EC.element_to_be_clickable(textbox_locator))
    textbox.clear()
    textbox.send_keys(value)
    textbox.send_keys(Keys.ENTER)


def print_results(wait: WebDriverWait):
    """Print results from search."""
    locator = (By.XPATH, "//*[contains(@class,'result-item') and @rel]")
    rows = wait.until(EC.visibility_of_all_elements_located(locator))
    for row in rows:
        print(parse_user_info(wait, row))


def parse_user_info(wait: WebDriverWait, row: WebElement):
    """Parse user info."""
    title = row.find_element_by_xpath(".//*[contains(@class, ' title ')]")
    sub_title = row.find_element_by_xpath(".//*[contains(@class, 'sub-title')]")
    description = row.find_element_by_xpath(".//*[contains(@class, 'desc')]")
    return f'{title.text:20} | {sub_title.text:20} | {description.text:20}'


if __name__ == '__main__':
    my_driver = get_driver('chrome')
    my_wait = WebDriverWait(my_driver, 3)

    # Go to tiktok
    my_driver.get('https://www.tiktok.com/?lang=es ')

    # Search
    search(my_wait, 'Python')

    # Show results info
    print_results(my_wait)

    # Quit
    my_driver.quit()
