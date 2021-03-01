"""Search in tiktok"""
from selenium.webdriver.remote.webelement import WebElement

from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def search(wait: WebDriverWait, value: str):
    """Search in tiktok

    :param wait: Web driver wait instance
    :param value: Value to search
    """
    input_locator = (By.NAME, 'q')
    textbox = wait.until(EC.element_to_be_clickable(input_locator))
    textbox.clear()
    textbox.send_keys(value)

    btn_locator = (By.XPATH, "//button[@type='submit']")
    btn = wait.until(EC.element_to_be_clickable(btn_locator))
    btn.click()


def print_results(wait: WebDriverWait):
    """Print search results information.

    :param wait:  Web driver wait instance
    """
    profiles_loc = (By.XPATH, "//a[contains(@class, 'result-item')]")
    profiles = wait.until(EC.visibility_of_all_elements_located(profiles_loc))
    print(f'Results: {len(profiles)}')
    for profile in profiles:
        title = profile.find_element_by_xpath(".//*[contains(@class, ' title ')]")
        sub_title = profile.find_element_by_xpath(".//*[contains(@class, 'sub-title')]")
        description = profile.find_element_by_xpath(".//*[contains(@class, 'desc')]")
        print(f'{title.text:20} | {sub_title.text:20} | {description.text:20}')


if __name__ == '__main__':
    my_driver = get_driver('chrome')
    my_wait = WebDriverWait(my_driver, 3)

    my_driver.get('https://www.tiktok.com/?lang=es')

    search(my_wait, 'Python')

    print_results(my_wait)

    my_driver.quit()
