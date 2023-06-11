import allure
import pytest

from pages.add_to_cart_item_in_home_page import AddCartClass

@allure.title("Cart Page")
class TestCartPage:
    @pytest.fixture
    def set_up(self, driver):
        set_up = AddCartClass(driver, "https://www.saucedemo.com/inventory.html")
        set_up.open_browser()
        return set_up

    @pytest.mark.usefixtures('driver')
    @allure.title("Add to cart")
    @allure.feature("Cart page")
    @allure.tag("Cart")
    def test_add_to_card(self, set_up):
        set_up.add_to_cart()
        set_up.case_in_button_text()

    @pytest.mark.usefixtures('driver')
    @allure.title("Add to cart more item")
    @allure.feature("Cart page")
    @allure.tag("Cart")
    def test_add_to_card_more_item(self, set_up):
        set_up.add_to_cart_more_item()
        set_up.case_true_cart_icon_item()

    @pytest.mark.usefixtures('driver')
    @allure.title("Add to cart and remove")
    @allure.feature("Cart page")
    @allure.tag("Cart")
    def test_add_to_card_item_and_remove(self, set_up):
        set_up.add_to_cart_item_and_remove()
        set_up.case_true_cart_icon_item_remove()

    @pytest.mark.usefixtures('driver')
    @allure.title("Add to cart and navigate to cart")
    @allure.feature("Cart page")
    @allure.tag("Cart")
    def test_add_to_card_item_ckeck_cart(self, set_up):
        set_up.add_to_cart_item_and_ckeck_icon_cart()
        set_up.case_true_cart_icon_item_not_zero()
