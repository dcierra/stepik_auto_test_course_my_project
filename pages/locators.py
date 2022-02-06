from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")


class ProductPageLocators():
    BASKET_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    MESSAGE_PRODUCT_NAME = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']//strong")
    BASKET_PRICE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//strong")