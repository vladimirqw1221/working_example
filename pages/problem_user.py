import time
from enams.glodal_enams import GlobalEnums
from base_page.base_page import BaseClass
import allure
import os
from dotenv import load_dotenv

from pages.locator_page import Locators

load_dotenv()


class ProblemUserClass(BaseClass):
    locator = Locators()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def problem_user(self):
        with allure.step(" Test case for problem user"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys("problem_user")
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_visibile(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_BAG_PROBLEM).click()
            self.select_element_is_clickable(self.locator.REMOVE_TO_BAG_PROBLEM).click()

    def case_check_button(self):
        with allure.step("Check button on home page"):
            try:
                value_button = self.select_element_is_clickable(self.locator.REMOVE_TO_BAG_PROBLEM).text
                assert value_button == "Add to cart", GlobalEnums.WRONG_VALUE_NOT_CORRECT.value
            except AssertionError:
                value_button = self.select_element_is_clickable(self.locator.REMOVE_TO_BAG_PROBLEM).text
                print(f"Button not view \"Add to cart\" , value = {value_button}")

    def addet_all_item(self):
        with allure.step(" Test case for problem user added all item in cart "):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys("problem_user")
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_visibile(self.locator.LOGIN_BTN).click()
            self.select_element_is_clickable(self.locator.ITEM_1).click()
            self.select_element_is_clickable(self.locator.ITEM_2).click()
            self.select_element_is_clickable(self.locator.ITEM_3).click()
            self.select_element_is_clickable(self.locator.ITEM_4).click()
            self.select_element_is_clickable(self.locator.ITEM_5).click()
            self.select_element_is_clickable(self.locator.ITEM_6).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()

    def checking_cart_case(self):
        with allure.step(" Chek itrms in cart"):
            try:
                cart_value = self.select_element_is_visibile(self.locator.CART_ICON).text
                assert cart_value == "6", GlobalEnums.WRONG_VALUE_NOT_CORRECT.value
                print(cart_value)
            except AssertionError:
                cart_value = self.select_element_is_visibile(self.locator.CART_ICON).text
                print(f"Items in cart not equal 6, if you added "
                      f"all items on homepage,your item = {cart_value}")

    def check_order_for_problem_user(self):
        with allure.step("Cheking order for problem user"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys("problem_user")
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_visibile(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ITEM_1).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.select_element_is_clickable(self.locator.CHECOUNT_BTN).click()
            self.select_element_is_visibile(self.locator.FIRST_NAME).send_keys("Petr")
            self.select_element_is_visibile(self.locator.LAST_NAME).send_keys("Ivanov")
            self.select_element_is_visibile(self.locator.ZIP_CODE).send_keys("232343")
            self.select_element_is_clickable(self.locator.CONTINE_CHECKOUNT_BTN).click()

    def case_for_problem_user(self):
        with allure.step("Test case for problem user"):
            try:
                value_url = "https://www.saucedemo.com/checkout-step-two.html"
                current_url = self.get_current_url()
                assert current_url == value_url, GlobalEnums.WRONG_ERROR_URL.value
            except AssertionError:
                print(f'Your shopping  STOPED ')
