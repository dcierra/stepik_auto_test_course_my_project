import pytest
import faker
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


@pytest.mark.registered_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        f = faker.Faker()
        email = f.email()
        password = "Testtest123!"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.should_be_add_to_basket_notification()
        product_page.product_name_is_correct_in_notification()
        product_page.should_be_your_basket_total_notification()
        product_page.basket_price_is_equal_to_product_price()


@pytest.mark.need_review
@pytest.mark.parametrize('offer_number', ["0", "1", "2", "3", "4", "5", "6",
                                          pytest.param("7", marks=pytest.mark.xfail),
                                          "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer"
    product_link = link+offer_number
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_add_to_basket_notification()
    product_page.product_name_is_correct_in_notification()
    product_page.should_be_your_basket_total_notification()
    product_page.basket_price_is_equal_to_product_price()


@pytest.mark.skip(reason="test is failed due to incorrect test logic")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.skip(reason="test is failed due to incorrect test logic")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.add_to_basket_message_disappears()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_your_basket_is_empty_message()