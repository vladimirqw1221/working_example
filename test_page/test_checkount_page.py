import pytest
import allure
from pages.checkout_information import InformationCalss


class TestCheckountPage:
    @pytest.fixture
    def set_up(self, driver):
        set_up = InformationCalss(driver, "https://www.saucedemo.com/")
        set_up.open_browser()
        return set_up

    @pytest.mark.usefixtures('driver')
    @allure.title("Checkout info page")
    @allure.feature("Checkout")
    @allure.tag("checkout")
    def test_checkount_info(self, set_up):
        set_up.checkout_info_page()
        set_up.case_checkout_info_page()

    @pytest.mark.usefixtures('driver')
    @allure.title("Error massage first name")
    @allure.feature("Info page")
    @allure.tag("Info page")
    def test_checkount_info_error_msg_for_first_name(self, set_up):
        set_up.checkout_info_page_error_first_name()
        set_up.error_msg_last_name()

    @pytest.mark.usefixtures('driver')
    @allure.title("Error zip code")
    @allure.feature("info page")
    @allure.tag("Info page")
    def test_checkount_info_error_msg_for_zip_code(self, set_up):
        set_up.checkout_info_page_error_last_name()
        set_up.case_eroor_msg_zip_code_name()

    @pytest.mark.usefixtures('driver')
    @allure.title("Added all info")
    @allure.feature("info page")
    @allure.tag("Info page")
    def test_checkount_info_all_info(self, set_up):
        set_up.checkout_info_page_enter_all_info()
        set_up.case_all_info()

    @pytest.mark.usefixtures('driver')
    @allure.title("Error massage not first name")
    @allure.feature("Info page")
    @allure.tag("Info page")
    def test_checkount_no_first_name(self, set_up):
        set_up.checkout_info_page_not_first_name()
        set_up.case_no_first_name()

    @pytest.mark.usefixtures('driver')
    @allure.title("Added full info")
    @allure.feature("Info page")
    @allure.tag("Info page")
    def test_checkount_full_info(self, set_up):
        set_up.full_info_for_registr_user()
        set_up.case_full_info()

    @pytest.mark.usefixtures('driver')
    @allure.title("Added full info for user guest")
    @allure.feature("Info page")
    @allure.tag("Info page")
    def test_checkount_full_info_guest_user(self, set_up):
        set_up.full_info_guest_user()
        set_up.case_full_info_guest_user()


