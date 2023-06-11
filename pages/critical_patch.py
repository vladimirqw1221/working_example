import time

from base_page.base_page import BaseClass
import os
from dotenv import load_dotenv
import allure

from generator.generator import generator
from pages.locator_page import Locators

load_dotenv()
class CriticallPatchClass(BaseClass):
    locator = Locators()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url


    def criticall_patch_for_register_user(self):
        with allure.step("Critical patch for register user"):
            """Authorization"""
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_visibile(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            """Add to cart all item for critical patch  """
            self.select_element_is_clickable(self.locator.ITEN_1).click()
            self.select_element_is_clickable(self.locator.ITEN_2).click()
            self.select_element_is_clickable(self.locator.ITEN_3).click()
            self.select_element_is_clickable(self.locator.ITEN_4).click()
            self.select_element_is_clickable(self.locator.ITEN_5).click()
            self.select_element_is_clickable(self.locator.ITEN_6).click()
            self.get_current_url()
            """Navigate to cart"""
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.select_element_is_clickable(self.locator.CHECOUNT_BTN).click()
            self.get_current_url()
            """Navigate to Checkout: Your Information"""
            self.select_element_is_visibile(self.locator.FIRST_NAME).send_keys("Pert")
            self.select_element_is_visibile(self.locator.LAST_NAME).send_keys("Ivanov")
            self.select_element_is_visibile(self.locator.ZIP_CODE).send_keys("123231")
            self.select_element_is_clickable(self.locator.CONTINE_CHECKOUNT_BTN).click()
            self.get_current_url()
            """Navigate to Checkout: Overview"""
            self.select_element_is_clickable(self.locator.FINISH_BTN).click()
            self.get_current_url()
            """Navigate to Checkout: Complete!"""
            self.select_element_is_clickable(self.locator.GO_HOME_BTN).click()
            self.take_scrn_shot()

    def case_criticall_patch_for_register_user(self):
        with allure.step("Check info, after finish critical patch, if use register user"):
            word = self.select_element_is_visibile(self.locator.PRODUCTS)
            self.check_word(word, "Products")
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/inventory.html")


    def criticall_patch_for_guest_user(self):
        with allure.step("Critical patch for guest user"):
            person_info = next(generator())
            first_name = person_info.first_name
            last_name = person_info.last_name
            zip_code = person_info.zip_cade
            """Authorization"""
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_visibile(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            """Add to cart all item for critical patch  """
            self.select_element_is_clickable(self.locator.ITEN_1).click()
            self.select_element_is_clickable(self.locator.ITEN_2).click()
            self.select_element_is_clickable(self.locator.ITEN_3).click()
            self.select_element_is_clickable(self.locator.ITEN_4).click()
            self.select_element_is_clickable(self.locator.ITEN_5).click()
            self.select_element_is_clickable(self.locator.ITEN_6).click()
            self.get_current_url()
            """Navigate to cart"""
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.select_element_is_clickable(self.locator.CHECOUNT_BTN).click()
            self.get_current_url()
            """Navigate to Checkout: Your Information"""
            time.sleep(5)
            self.select_element_is_visibile(self.locator.FIRST_NAME).send_keys(first_name)
            self.select_element_is_visibile(self.locator.LAST_NAME).send_keys(last_name)
            self.select_element_is_visibile(self.locator.ZIP_CODE).send_keys(zip_code)
            self.select_element_is_clickable(self.locator.CONTINE_CHECKOUNT_BTN).click()
            self.get_current_url()
            """Navigate to Checkout: Overview"""
            time.sleep(5)
            self.select_element_is_clickable(self.locator.FINISH_BTN).click()
            self.get_current_url()
            """Navigate to Checkout: Complete!"""
            self.select_element_is_clickable(self.locator.GO_HOME_BTN).click()
            self.take_scrn_shot()

    def case_criticall_patch_for_guest_user(self):
        with allure.step("Check info, after finish critical patch, if use guested user"):
            word = self.select_element_is_visibile(self.locator.PRODUCTS)
            self.check_word(word, "Products")
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/inventory.html")



