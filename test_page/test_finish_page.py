import pytest
import allure
from pages.finish_oreder_page import FinishOrderPageClass


class TestFinishPage:
    @pytest.fixture
    def set_up(self,driver):
        set_up = FinishOrderPageClass(driver, "https://www.saucedemo.com/")
        set_up.open_browser()
        return set_up

    @pytest.mark.usefixtures('driver')
    @allure.title("Check result navigate on home page after payment order")
    @allure.feature("Payment page")
    @allure.tag("Payment page")
    def test_checking_finish_page_and_go_home_page(self,set_up):
        set_up.checking_finish_page_and_go_home_page()
        set_up.case_finish_page_and_go_home_page()

    @pytest.mark.usefixtures('driver')
    @allure.title("Check result navigate to on cart page after payment order")
    @allure.feature("Payment page")
    @allure.tag("Payment page")
    def test_checking_finish_page_and_go_cart_page(self, set_up):
        set_up.checking_finish_page_and_go_cart_page()
        set_up.case_finish_page_and_go_cart_page()