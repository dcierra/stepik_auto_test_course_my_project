from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_LIST_IN_BASKET), "Products in basket are presented, but should not be"

    def should_be_your_basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.YOUR_BASKET_IS_EMPTY_MESSAGE), "'Your basket is empty' message is absent"
        your_basket_is_empty_message_text = self.find_text(*BasketPageLocators.YOUR_BASKET_IS_EMPTY_MESSAGE)
        your_basket_is_empty_message_text = your_basket_is_empty_message_text.split(".")
        assert your_basket_is_empty_message_text[0] + '.' == "Your basket is empty.", \
            f"Wrong pattern message. Got '{your_basket_is_empty_message_text[0]}.' instead of 'Your basket is empty.'"