"""Browsing example using Selenium"""
from pathlib import Path
from selenium import webdriver


def get_project_root() -> Path:
    """Get project root path."""
    return Path(__file__).parent.parent


def get_chrome_path() -> Path:
    """Get chrome driver path."""
    root = get_project_root()
    return root.joinpath('drivers', 'chromedriver.exe')


def get_firefox_path() -> Path:
    """Get firefox driver path."""
    root = get_project_root()
    return root.joinpath('drivers', 'geckodriver.exe')


def print_page_details(driver: webdriver.Remote) -> None:
    """Get page with details"""
    print(f'Title: {driver.title}')
    print(f'Current URL: {driver.current_url}')
    print(f'Source: {driver.page_source}')


driver = webdriver.Chrome(executable_path=get_chrome_path())

driver.get('https://www.google.com/')
print_page_details(driver)

driver.get('https://www.mlb.com/es')
print_page_details(driver)

driver.get('https://www.nytimes.com/es/')
driver.refresh()
print_page_details(driver)

driver.back()
driver.back()
print_page_details(driver)

driver.quit()
