import os
import time
import allure

from generator.generator import generator
from pages.locator_page import Locators

from pages.add_to_cart_item_in_home_page import AddCartClass


class InformationCalss(AddCartClass):
    locarot = Locators()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def checkout_info_page(self):
        with allure.step("navigate to checkout page"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.select_element_is_clickable(self.locator.CHECOUNT_BTN).click()

    def case_checkout_info_page(self):
        with allure.step("Checking text on Information page"):
            word = self.select_element_is_visibile(self.locator.CHACOUNT_YOUR_INFI)
            self.check_word(word, "Checkout: Your Information")
            self.equal_url("https://www.saucedemo.com/checkout-step-one.html")

    def checkout_info_page_error_first_name(self):
        with allure.step("Error massage, if not last name in filed"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.select_element_is_clickable(self.locator.CHECOUNT_BTN).click()
            self.select_element_is_visibile(self.locator.FIRST_NAME).send_keys("Petr")
            self.select_element_is_clickable(self.locator.CONTINE_CHECKOUNT_BTN).click()

    def error_msg_last_name(self):
        with allure.step(" Checking massage error, if not last name filed"):
            word = self.select_element_is_visibile(self.locator.ERROR_LAST_NAME)
            self.check_word(word, "Error: Last Name is required")
            self.get_current_url()


    def checkout_info_page_error_last_name(self):
        with allure.step("Error massage, if not zip-cade"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.select_element_is_clickable(self.locator.CHECOUNT_BTN).click()
            self.select_element_is_visibile(self.locator.FIRST_NAME).send_keys("Petr")
            self.select_element_is_clickable(self.locator.LAST_NAME).send_keys("Ivanov")
            self.select_element_is_clickable(self.locator.CONTINE_CHECKOUNT_BTN).click()

    def case_eroor_msg_zip_code_name(self):
        with allure.step("Checking text, if blank zip-code filed"):
            word = self.select_element_is_visibile(self.locator.ZIP_CODE_ERROR)
            self.check_word(word, "Error: Postal Code is required")
            self.get_current_url()


    def checkout_info_page_enter_all_info(self):
        with allure.step("Checking next page if all filed added"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.select_element_is_clickable(self.locator.CHECOUNT_BTN).click()
            self.select_element_is_visibile(self.locator.FIRST_NAME).send_keys("Petr")
            self.select_element_is_clickable(self.locator.LAST_NAME).send_keys("Ivanov")
            self.select_element_is_clickable(self.locator.ZIP_CODE).send_keys("212121")
            self.select_element_is_clickable(self.locator.CONTINE_INFO_BTN).click()

    def case_all_info(self):
        with allure.step("Checking text, if all info added"):
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/checkout-step-two.html")

    def checkout_info_page_not_first_name(self):
        with allure.step("Error massage, if not first-name"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.select_element_is_clickable(self.locator.CHECOUNT_BTN).click()
            self.select_element_is_clickable(self.locator.LAST_NAME).send_keys("Ivanov")
            self.select_element_is_clickable(self.locator.ZIP_CODE).send_keys("212121")
            self.select_element_is_clickable(self.locator.CONTINE_INFO_BTN).click()

    def case_no_first_name(self):
        with allure.step("Check error text, if blank filed first name"):
            word = self.select_element_is_visibile(self.locator.ERROR_MSD_FIRST_NAME)
            self.check_word(word, "Error: First Name is required")
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/checkout-step-one.html")

    def full_info_for_registr_user(self):
        with allure.step("Navigate to checkout page for register user"):
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.select_element_is_clickable(self.locator.CHECOUNT_BTN).click()
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/checkout-step-one.html")
            self.select_element_is_clickable(self.locator.FIRST_NAME).send_keys("Petr")
            self.select_element_is_clickable(self.locator.LAST_NAME).send_keys("Ivanov")
            self.select_element_is_clickable(self.locator.ZIP_CODE).send_keys("405778")
            self.select_element_is_clickable(self.locator.CONTINE_INFO_BTN).click()

    def case_full_info(self):
        with allure.step("Check text for register user, in checkout page"):
            word = self.select_element_is_visibile(self.locator.OVERVIEW)
            self.check_word(word, "Checkout: Overview")
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/checkout-step-two.html")

    def full_info_guest_user(self):
        with allure.step("Navigate to checkout page for guest user"):
            person_info = next(generator())
            first_name = person_info.first_name
            last_name = person_info.last_name
            zip_code = person_info.zip_cade
            self.select_element_is_visibile(self.locator.USER_NAME).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibile(self.locator.PASSWORD).send_keys(os.getenv('SECRET_PWD'))
            self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.ADD_TO_CART).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.select_element_is_clickable(self.locator.CHECOUNT_BTN).click()
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/checkout-step-one.html")
            self.select_element_is_clickable(self.locator.FIRST_NAME).send_keys(first_name)
            self.select_element_is_clickable(self.locator.LAST_NAME).send_keys(last_name)
            self.select_element_is_clickable(self.locator.ZIP_CODE).send_keys(zip_code)
            self.select_element_is_clickable(self.locator.CONTINE_INFO_BTN).click()

    def case_full_info_guest_user(self):
        with allure.step("Check text for guest user, in checkout page"):
            word = self.select_element_is_visibile(self.locator.OVERVIEW)
            self.check_word(word, "Checkout: Overview")
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/checkout-step-two.html")
