import pytest
import allure
from pages.overview_order_page import OverviewOrderClass


class TestOverviewPade:
    @pytest.fixture
    def set_up(self, driver):
        set_up = OverviewOrderClass(driver, "https://www.saucedemo.com/")
        set_up.open_browser()
        return set_up


    @pytest.mark.usefixtures('driver')
    @allure.title("Checking payment info")
    @allure.feature("Finish page")
    @allure.tag("Finish page")
    def test_checking_pyment_info(self, set_up):
        set_up.checking_pyment_info()
        set_up.case_checking_pyment_info()

    @pytest.mark.usefixtures('driver')
    @allure.title("Check payment info and back")
    @allure.feature("Finish page")
    @allure.tag("Finish page")
    def test_checking_pyment_info_and_back(self, set_up):
        set_up.checking_pyment_info_and_back()
        set_up.case_checking_pyment_info_and_back()

    @pytest.mark.usefixtures('driver')
    @allure.title("Check payment info and back to PDP, and remove item")
    @allure.feature("Finish page")
    @allure.tag("Finish page")
    def test_checking_pyment_info_and_back_and_remove(self, set_up):
        set_up.checking_pyment_info_and_back_and_remove_item()
        set_up.case_checking_pyment_info_and_back_and_remove()

    @pytest.mark.usefixtures('driver')
    @allure.title("Check payment info and back to cart page")
    @allure.feature("Finish page")
    @allure.tag("Finish page")
    def test_checking_pyment_info_and_back_and_back_to_cart(self, set_up):
        set_up.checking_pyment_info_and_back_and_back_to_cart()
        set_up.case_checking_pyment_info_and_back_and_back_to_cart()

    @pytest.mark.usefixtures('driver')
    @allure.title("Finish order")
    @allure.feature("Finish page")
    @allure.tag("Finish page")
    def test_checking_info_finish_order(self, set_up):
        set_up.checking_pyment_info_finish_order()
        set_up.case_checking_info_finish_order()





