from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def get_product_title(self):
        return self.get_element_text(ProductPageLocators.PRODUCT_TITLE)

    def get_product_price(self):
        return self.get_element_text(ProductPageLocators.PRODUCT_PRICE)

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "\"Add to basket\" button not found!"

    def add_product_to_basket(self):
        self.do_click(ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS), "Success message not found!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ALERT_SUCCESS), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), "Success message did not disappear"

    def get_product_name_from_success_message(self):
        return self.get_element_text(ProductPageLocators.ALERT_SUCCESS_PRODUCT_NAME)

    def should_be_basket_cost(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_BASKET_COST), "Basket cost alert not found!"

    def product_name_in_success_alert_should_match_added_product_name(self):
        alert_product_name = self.get_product_name_from_success_message()
        product_title = self.get_product_title()
        assert alert_product_name == product_title, "Product name doesn't match product title!"

    def get_basket_cost(self):
        return self.get_element_text(ProductPageLocators.BASKET_COST)

    def basket_cost_should_match_product_price(self):
        basket_cost = self.get_basket_cost()
        product_price = self.get_product_price()
        assert basket_cost == product_price, "Basket cost doesn't match product price!"
