import time

import allure

from base_page.base_page import BaseClass
import os
from dotenv import load_dotenv

from pages.locator_page import Locators

load_dotenv()
class BurgerMenuClass(BaseClass):
    locator = Locators()


    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def open_and_close_menu(self):
        with allure.step("Checking button close in menu"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_visibile(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.MENU_BTN).click()
            self.select_element_is_clickable(self.locator.CLOSE_BTN).click()

    def case_open_and_close_menu(self):
        with allure.step("Text check after menu close"):
            word = self.select_element_is_visibile(self.locator.PRODUCTS)
            self.check_word(word, "Products")
            self.get_current_url()



    def open_menu_go_to_about_page(self):
        with allure.step("Navigate to about page"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_visibile(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.MENU_BTN).click()
            self.select_element_is_clickable(self.locator.ABOUT_LINK).click()
            self.get_current_url()
            self.navigate_to_back()
            self.get_current_url()

    def case_open_menu_go_to_about_page(self):
        with allure.step("Check text after back home-page"):
            word = self.select_element_is_visibile(self.locator.PRODUCTS)
            self.check_word(word, "Products")
            self.get_current_url()


    def open_menu_and_logout(self):
        with allure.step("Check logout in burger menu"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_visibile(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.MENU_BTN).click()
            self.select_element_is_clickable(self.locator.LOGOUT_LINK).click()
            self.get_current_url()
            self.get_current_url()

    def case_open_menu_and_logout(self):
        with allure.step("Check text after logout user"):
            word = self.select_element_is_visibile(self.locator.LOGIN_PAGE_LOCATOR)
            self.check_word(word, "Accepted usernames are:")
            self.get_current_url()





