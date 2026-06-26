from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[text()='Add to cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def get_title(self):
        return self.get_text(self.TITLE)

    def count_products(self):
        return len(self.find_elements(self.INVENTORY_ITEMS))

    def add_first_product_to_cart(self):
        botones = self.find_elements(self.ADD_TO_CART_BUTTONS)
        botones[0].click()

    def get_cart_badge_number(self):
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        self.click(self.CART_LINK)