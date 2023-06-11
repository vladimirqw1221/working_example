import pytest
import allure
from pages.burger_menu import BurgerMenuClass


class TestBurgerMenu:

    @pytest.fixture
    def set_up(self, driver):
        set_up = BurgerMenuClass(driver, "https://www.saucedemo.com/")
        set_up.open_browser()
        return set_up

    @pytest.mark.usefixtures('driver')
    @allure.title("Open and close menu")
    @allure.feature("Burger menu")
    @allure.tag("Burger menu")
    def test_open_and_close_menu(self,set_up):
        set_up.open_and_close_menu()
        set_up.case_open_and_close_menu()

    @pytest.mark.usefixtures('driver')
    @allure.title("Navigate to about page")
    @allure.feature("Burger menu")
    @allure.tag("Burger menu")
    def test_open_menu_go_to_about_page(self, set_up):
        set_up.open_menu_go_to_about_page()
        set_up.case_open_menu_go_to_about_page()

    @pytest.mark.usefixtures('driver')
    @allure.title("Navigate to login page")
    @allure.feature("Burger menu")
    @allure.tag("Burger menu")
    def test_open_menu_and_logout(self, set_up):
        set_up.open_menu_and_logout()
        set_up.open_menu_and_logout()