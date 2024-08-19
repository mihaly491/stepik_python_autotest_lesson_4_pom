from selenium.webdriver.common.by import By


class BasePageLocators():
    LANGUAGE_SELECT = (By.NAME, "language")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM_INVALID = (By.CSS_SELECTOR, "#login_form_invalid")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.NAME, "registration-email")
    REGISTER_PASSWORD1_INPUT = (By.NAME, "registration-password1")
    REGISTER_PASSWORD2_INPUT = (By.NAME, "registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.NAME, "registration_submit")
    REGISTER_FORM_INVALID = (By.CSS_SELECTOR, "#register_form_invalid")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    ALERT_SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    ALERT_BASKET_COST = (By.CSS_SELECTOR, ".alert-info")
    BASKET_COST = (By.CSS_SELECTOR, ".alert-info strong")
