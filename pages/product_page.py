from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_basket_button(self):
        assert self.browser.find_elements(*ProductPageLocators.BASKET_BUTTON), "Basket Button is not presented"

    def should_be_product_name(self):
        assert self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME), "Product Name is not presented"

    def should_be_product_price(self):
        assert self.browser.find_elements(*ProductPageLocators.PRODUCT_PRICE), "Product Price is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_msg_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"

    def should_be_product_name_in_msg(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_msg = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == product_name_in_msg, "Product name not found in message"

    def compare_product_price_and_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, "Product price and basket price different"

    def add_basket_button(self):
        self.should_be_basket_button()
        self.should_be_product_name()
        self.should_be_product_price()
        btn = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        btn.click()
