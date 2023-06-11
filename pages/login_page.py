import time
import allure
from base_page.base_page import BaseClass
from pages.locator_page import Locators
from dotenv import load_dotenv
import os

load_dotenv()


class MainClass(BaseClass):
    locator = Locators()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def login(self):
        with allure.step("Login method  for correct user"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()

    def case_word_on_home_page(self):
        with allure.step("Check text in home page, after login in system"):
            word = self.select_element_is_visibile(self.locator.PRODUCTS)
            self.check_word(word, "Products")
            self.equal_url("https://www.saucedemo.com/inventory.html")
            print("Test case for authorization passed")

    def negative_case_login(self):
        with allure.step("Error massage in login page "):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys("ieiiew")
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()

    def case_text_incorrect_possword(self):
        with allure.step("Check text in login page, if user not login"):
            word = self.select_element_is_visibile(self.locator.ERROR_MSD_INCOR_POWORD)
            self.check_word(word, "Epic sadface: Username and password do not match any user in this service")
            self.equal_url("https://www.saucedemo.com/")

    def negative_case_incorrect_user_name(self):
        with allure.step("Error massage, if user incorrect login"):
            self.select_element_is_visibile(self.locator.USER_NAME)
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()

    def case_text_incorrect_user_name(self):
        with allure.step("Check text, if user used incorrect login"):
            word = self.select_element_is_visibile(self.locator.ERROR_MSD_INCOR_USER_NAME)
            self.check_word(word, "Epic sadface: Username is required")
            self.equal_url("https://www.saucedemo.com/")
