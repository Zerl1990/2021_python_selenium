"""Web Driver Example"""
from pathlib import Path
from selenium import webdriver


def get_project_root() -> Path:
    """Get project root path."""
    return Path(__file__).parent.parent


def get_chrome_path() -> Path:
    """Get chrome driver path."""
    root = get_project_root()
    return root.joinpath('drivers', 'chromedriver.exe')


driver = webdriver.Chrome(executable_path=get_chrome_path())
driver.get('https://saucelabs.com/resources/articles/selenium-grid')
print(f'Current tile: {driver.title}')
print(f'Current url: {driver.current_url}')
print(f'Current source: {driver.page_source}')
driver.get('https://saucelabs.com/solutions/enterprise')
driver.back()
driver.forward()
driver.refresh()
driver.quit()
