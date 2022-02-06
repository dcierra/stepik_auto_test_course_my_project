from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"


class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, ".alert-success")
    REGISTRATION_SUBMIT_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")
    PRODUCT_NAME_IN_ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    YOUR_BASKET_TOTAL_NOTIFICATION = (By.CSS_SELECTOR, ".alert-info")
    BASKET_PRICE_IN_BASKET_TOTAL_NOTIFICATION = (By.CSS_SELECTOR, ".alert-info strong")


class BasketPageLocators():
    PRODUCTS_LIST_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    YOUR_BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")