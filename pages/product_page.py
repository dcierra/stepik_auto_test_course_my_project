from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_notification(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "'Add to basket' notification is absent"

    def should_be_your_basket_total_notification(self):
        assert self.is_element_present(*ProductPageLocators.YOUR_BASKET_TOTAL_NOTIFICATION), "'Your basket total' notification is absent"

    def product_name_is_correct_in_notification(self):
        origin_product_name = self.find_text(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_notification = self.find_text(*ProductPageLocators.PRODUCT_NAME_IN_ADDED_TO_BASKET_MESSAGE)
        assert origin_product_name == product_name_in_notification, "Product name in notification doesn't match to original product name"

    def basket_price_is_equal_to_product_price(self):
        origin_product_price = self.find_text(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.find_text(*ProductPageLocators.BASKET_PRICE_IN_BASKET_TOTAL_NOTIFICATION)
        assert origin_product_price == basket_price, "Product price is not equal to basket price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "Success message is presented, but should not be"

    def add_to_basket_message_disappears(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "'Add to basket' notification isn't disappeared"