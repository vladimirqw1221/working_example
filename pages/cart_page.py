import os
import time
from selenium.common.exceptions import TimeoutException
import allure
from dotenv import load_dotenv
from pages.add_to_cart_item_in_home_page import AddCartClass
from pages.locator_page import Locators

load_dotenv()


class CartPageClass(AddCartClass):
    locator = Locators()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def check_add_to_cart_in_cart_page(self):
        with allure.step("Navigate to cart page"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()

    def case_text_navigate_to_cart(self):
        with allure.step(" Checking text in cart page "):
            word = self.select_element_is_visibile(self.locator.CART_PAGE)
            self.check_word(word, "Your Cart")
            self.get_current_url()

    def case_text_navigate_to_cart_and_chek_qua(self):
        with allure.step("Checking count item in cart page"):
            word = self.select_element_is_visibile(self.locator.CART_ICON_QUANTITY)
            self.check_word(word, "1")


    def check_add_to_cart_in_cart_page_and_remove(self):
        with allure.step("Added item in cart and remove in cart item"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.select_element_is_clickable(self.locator.REMOVE_BTN_IN_CART).click()

    def case_text_navigate_to_cart_and_remove(self):
        with allure.step("Checking button in not item in cart"):
            try:
                word = self.select_element_is_visibile(self.locator.REMOVE_BTN)
                self.check_word(word, "Remove")
                print("Cart not clear")
            except TimeoutException:
                print("Cart clear")

    def check_add_to_cart_in_cart_page_and_contine_shop(self):
        with allure.step("Navigate to cart, after added item "):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.select_element_is_clickable(self.locator.CONTINE_SHOP).click()

    def case_text_navigate_to_cart_and_cantine_shop(self):
        with allure.step("Count quantity item in cart page "):
            word = self.select_element_is_visibile(self.locator.CART_ICON)
            self.check_word(word, "1")













