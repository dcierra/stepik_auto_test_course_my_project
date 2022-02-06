from .base_page import BasePage
from .locators import LoginPageLocators
import faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == LoginPageLocators.LOGIN_URL, \
            f'Wrong URL: got {self.browser.current_url} instead of {LoginPageLocators.LOGIN_URL}'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is absent"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is absent"

    def register_new_user(self, email, password):
        self.input_the_text(*LoginPageLocators.REGISTER_EMAIL_FIELD, email)
        self.input_the_text(*LoginPageLocators.REGISTER_PASSWORD_FIELD, password)
        self.input_the_text(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_FIELD, password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        submit_button.click()
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUCCESS_NOTIFICATION), \
            "'Registration successful' message os absent. Probably registration wasn't completed"