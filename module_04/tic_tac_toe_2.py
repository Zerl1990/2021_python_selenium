"""Automatically play tic tac toe"""
import random
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def winner(wait):
    """Verify if we have a winner"""
    # css: .restart
    try:
        locator = (By.XPATH, "//div[@class='board win']")
        wait.until(EC.visibility_of_element_located(locator))
        return True
    except TimeoutException:
        return False


def select_empty_box(wait):
    """Select an empty box"""
    try:
        # xpath: //div[contains(@class, 'square')]
        locator = (By.CSS_SELECTOR, '.square')
        elements = wait.until(EC.visibility_of_all_elements_located(locator))
        empty = []  # List with web elements
        for box in elements:
            box: WebElement
            cell = box.find_element_by_tag_name('div')
            if not cell.get_attribute('class'):
                empty.append(box)
        print(f'Total empty boxes: {len(empty)}')
        target = random.choice(empty)
        target: WebElement
        target.click()
    except TimeoutException as exception:
        raise RuntimeError(f'No empty boxes: {exception}')


def print_game_stats(wait):
    """Print game stats"""
    # player 1 xpath: //p[contains(@class, 'player1')]/span[@class='score']
    player_1_locator = (By.CSS_SELECTOR, '.player1 .score')
    player_1 = wait.until(EC.visibility_of_element_located(player_1_locator))

    # ties css: .ties .score
    ties_locator = (By.XPATH, "//p[contains(@class, 'ties')]/span[contains(@class, 'score')]")
    ties = wait.until(EC.visibility_of_element_located(ties_locator))

    # player 2 xpath: //p[contains(@class, 'player2')]/span[@class='score']
    player_2_locator = (By.CSS_SELECTOR, '.player2 .score')
    player_2 = wait.until(EC.visibility_of_element_located(player_2_locator))

    print(f'Player: {player_1.text}, Ties: {ties.text}, Computer: {player_2.text}')


if __name__ == '__main__':
    my_driver = get_driver('chrome')
    my_wait = WebDriverWait(my_driver, 1)
    my_driver.get('https://playtictactoe.org/')
    while not winner(my_wait):
        select_empty_box(my_wait)
    print_game_stats(my_wait)
    my_driver.quit()
