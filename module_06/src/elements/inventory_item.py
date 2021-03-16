"""Abstraction to interact with inventory items."""
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators.inventory_item import InventoryItemLoc


class InventoryItem:
    """Represents inventory item."""

    __ADDED_LABEL = 'ADD TO CART'

    __REMOVE_LABEL = 'REMOVE'

    def __init__(self, wait: WebDriverWait, root: WebElement):
        self.__title = BasePageElement(InventoryItemLoc.TITLE, wait=wait, root=root)
        self.__description = BasePageElement(InventoryItemLoc.DESCRIPTION, wait=wait, root=root)
        self.__price = BasePageElement(InventoryItemLoc.PRICE, wait=wait, root=root)
        self.__inv_btn = BasePageElement(InventoryItemLoc.BTN, wait=wait, root=root)

    def get_title(self) -> str:
        """Get title for item."""
        return self.__title.get_text()

    def get_description(self) -> str:
        """Get description."""
        return self.__description.get_text()

    def get_price(self) -> str:
        """Get price."""
        return self.__price.get_text()

    def is_in_the_cart(self) -> str:
        """Get item status"""
        return self.__inv_btn.get_text() == InventoryItem.__REMOVE_LABEL

    def add_to_cart(self):
        """Add to cart."""
        if self.__inv_btn.get_text() == InventoryItem.__ADDED_LABEL:
            self.__inv_btn.click()
        else:
            raise ValueError(f'Inventory item is already in the cart')

    def remove_from_cart(self):
        """Remove from cart."""
        if self.__inv_btn.get_text() == InventoryItem.__REMOVE_LABEL:
            self.__inv_btn.click()
        else:
            raise ValueError(f'Inventory item is not in the cart')

    def open_details(self):
        """Open product details"""
        self.__title.click()
