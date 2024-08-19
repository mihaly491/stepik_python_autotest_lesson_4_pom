from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM_INVALID = (By.CSS_SELECTOR, "#login_form_invalid")
    REGISTER_FORM = (By.CSS_SELECTOR, "#registoer_form")
    REGISTER_FORM_INVALID = (By.CSS_SELECTOR, "#registoer_form_invalid")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    ALERT_SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    ALERT_BASKET_COST = (By.CSS_SELECTOR, ".alert-info")
    BASKET_COST = (By.CSS_SELECTOR, ".alert-info strong")
