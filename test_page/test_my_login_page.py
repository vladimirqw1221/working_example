import pytest
import allure
from pages.login_page import MainClass


class TestBreanch:
    @pytest.fixture()
    def set_up(self, driver):
        set_up = MainClass(driver, "https://www.saucedemo.com/")
        set_up.open_browser()
        return set_up

    @pytest.mark.usefixtures('driver')
    @allure.title("Login in system")
    @allure.feature("Login")
    @allure.tag("Login")
    def test_login_page(self, set_up):
        set_up.login()
        set_up.case_word_on_home_page()

    @pytest.mark.usefixtures('driver')
    @allure.title("Login in system Loginincorrect data")
    @allure.feature("Login")
    @allure.tag("Login")
    def test_login_page_incorect_pass(self, set_up):
        set_up.negative_case_login()
        set_up.case_text_incorrect_possword()






