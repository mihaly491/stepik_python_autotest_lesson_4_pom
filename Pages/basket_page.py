from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are items in the basket!"

    def should_be_text_that_the_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), \
            "Message that the basket is empty is not found!"
