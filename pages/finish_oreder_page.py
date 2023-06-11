import allure

from pages.locator_page import Locators
from pages.overview_order_page import OverviewOrderClass
import os
from dotenv import load_dotenv
import allure
load_dotenv()


class FinishOrderPageClass(OverviewOrderClass):
    locator = Locators()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url


    def checking_finish_page_and_go_home_page(self):
        with allure.step("Navigate to home page, after finish page"):
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
            self.select_element_is_clickable(self.locator.FINISH_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.GO_HOME_BTN).click()
            self.get_current_url()

    def case_finish_page_and_go_home_page(self):
        with allure.step("Checking text in home page"):
            word = self.select_element_is_visibile(self.locator.PRODUCTS)
            self.check_word(word, "Products")
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/inventory.html")
            self.take_scrn_shot()


    def checking_finish_page_and_go_cart_page(self):
        with allure.step("Navigate to cart, after finish page "):
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
            self.select_element_is_clickable(self.locator.FINISH_BTN).click()
            self.get_current_url()
            self.select_element_is_clickable(self.locator.CART_ICON).click()
            self.get_current_url()

    def case_finish_page_and_go_cart_page(self):
        with allure.step("Check text in cart page "):
            word = self.select_element_is_visibile(self.locator.CART_PAGE_INFO)
            self.check_word(word, "Your Cart")
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/cart.html")
            self.take_scrn_shot()




