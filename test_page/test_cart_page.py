import pytest
import allure

from pages.cart_page import CartPageClass


class TestCartPage:
    @pytest.fixture
    def set_up(self, driver):
        set_up = CartPageClass(driver, "https://www.saucedemo.com/")
        set_up.open_browser()
        return set_up


    @pytest.mark.usefixtures('driver')
    @allure.title("Added item on cart")
    @allure.feature("Cart page")
    @allure.tag("Cart")
    def test_cart_page(self, set_up):
        set_up.check_add_to_cart_in_cart_page()
        set_up.case_text_navigate_to_cart()
        set_up.case_text_navigate_to_cart_and_chek_qua()

    @pytest.mark.usefixtures('driver')
    @allure.title("Added and remove item on cart")
    @allure.feature("Cart page")
    @allure.tag("Cart")
    def test_cart_page_and_remove_item(self, set_up):
        set_up.check_add_to_cart_in_cart_page_and_remove()
        set_up.case_text_navigate_to_cart_and_remove()

    @pytest.mark.usefixtures('driver')
    @allure.title("Continue scoping ")
    @allure.feature("Cart")
    @allure.tag("Cart")
    def test_cart_page_and_contine_shop(self, set_up):
        set_up.check_add_to_cart_in_cart_page_and_contine_shop()
        set_up.case_text_navigate_to_cart_and_cantine_shop()