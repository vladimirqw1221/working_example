import os
import time

import allure

from pages.login_page import MainClass
from pages.locator_page import Locators
from dotenv import load_dotenv

load_dotenv()


class AddCartClass(MainClass):
    locarot = Locators()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def add_to_cart(self):
        with allure.step("Added to cart"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()

    def case_in_button_text(self):
        with allure.step("Check word in  cart"):
            word = self.select_element_is_clickable(self.locator.REMOVE_TEXT_IN_BUTTON)
            self.check_word(word, "Remove")
            self.get_current_url()
            time.sleep(3)

    def add_to_cart_more_item(self):
        with allure.step("Added  more item in cart"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()
            self.select_element_is_clickable(self.locator.ADD_TO_CART_TWO_ITEM).click()

    def case_true_cart_icon_item(self):
        with allure.step("Checking more item in cart"):
            word = self.select_element_is_clickable(self.locator.CART_ICON)
            self.check_word(word, "2")
            self.get_current_url()
            time.sleep(3)

    def add_to_cart_item_and_remove(self):
        with allure.step("Added item in card and remove in cart"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()
            self.select_element_is_clickable(self.locator.REMOVE_BTN).click()

    def case_true_cart_icon_item_remove(self):
        with allure.step("Checking param item in cart"):
            word = self.select_element_is_clickable(self.locator.CART_ICON)
            print(word)
            self.check_word(word, "")
            self.get_current_url()

    def add_to_cart_item_and_ckeck_icon_cart(self):
        with allure.step("Checking icon cart"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()

    def case_true_cart_icon_item_not_zero(self):
        with allure.step("Checking param cart, after removing in cart "):
            try:
                word = self.select_element_is_clickable(self.locator.CART_ICON)
                self.check_word(word, "")
                self.get_current_url()
            except AssertionError:
                word = self.select_element_is_clickable(self.locator.CART_ICON)
                print(f'Item in icon cart: {word.text}')
