"""Search in pinterest"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login(wait: WebDriverWait, email: str, secret: str):
    """Login to pinterest"""
    # Open login dialog
    login_btn_locator = (By.XPATH, "//*[@data-test-id='simple-login-button']//button")
    login_btn = wait.until(EC.element_to_be_clickable(login_btn_locator))
    login_btn.click()

    # Set users
    user_locator = (By.ID, 'email')
    user = wait.until(EC.element_to_be_clickable(user_locator))
    user.clear()
    user.send_keys(email)

    # Set password
    password_locator = (By.ID, 'password')
    password = wait.until(EC.element_to_be_clickable(password_locator))
    password.clear()
    password.send_keys(secret)

    # Submit
    submit_btn_locator = (By.XPATH, "//*[@data-test-id='registerFormSubmitButton']//button")
    submit_btn = wait.until(EC.element_to_be_clickable(submit_btn_locator))
    submit_btn.click()


def search(wait: WebDriverWait, value: str):
    """Search in pinterest."""
    textbox_locator = (By.XPATH, "//*[@data-test-id='search-box-input']")
    textbox = wait.until(EC.element_to_be_clickable(textbox_locator))
    textbox.clear()
    textbox.send_keys(value)
    textbox.send_keys(Keys.ENTER)


def get_results_tags(wait: WebDriverWait):
    """Get results tags."""
    try:
        tags_locator = (By.XPATH, "//*[@data-test-id='search-guide']")
        return wait.until(EC.visibility_of_all_elements_located(tags_locator))
    except TimeoutException:
        return []


def print_results_tags(wait: WebDriverWait):
    """Print results tags"""
    for element in get_results_tags(wait):
        print(f'Tag {element.text}')


def scrap(wait: WebDriverWait, cache=None):
    """Traverse all results"""
    visited = cache or []
    not_visited = [tag for tag in get_results_tags(wait) if tag.text not in visited]
    while not_visited:
        next_tag = not_visited[0]
        next_name = not_visited[0].text
        print(f'Goto -> {next_name}')
        next_tag.click()
        visited += scrap(wait, visited + [next_name])
        not_visited = [tag for tag in get_results_tags(wait) if tag.text not in visited]
    else:
        wait._driver.back()
    return visited


if __name__ == '__main__':
    my_driver = get_driver('chrome')
    my_wait = WebDriverWait(my_driver, 3)

    # Go to pinterest
    my_driver.get('https://www.pinterest.com.mx')

    # Login
    login(my_wait, 'qamindstester@gmail.com', 'Q@Minds4%')

    # Search selenium
    search(my_wait, 'Selenium')

    # Print results tags
    print_results_tags(my_wait)

    # Scrap web page
    scrap(my_wait)

    # Exit
    my_driver.quit()
