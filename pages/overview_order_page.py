import os
import allure
from pages.checkout_information import InformationCalss
from pages.locator_page import Locators
from dotenv import load_dotenv

load_dotenv()


class OverviewOrderClass(InformationCalss):
    locator = Locators()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def checking_pyment_info(self):
        with allure.step("navigate to payment page"):
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

    def case_checking_pyment_info(self):
        with allure.step("Check text in payment page"):
            word = self.select_element_is_visibile(self.locator.PAYINFO)
            self.check_word(word,"Payment Information")
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/checkout-step-two.html")


    def checking_pyment_info_and_back(self):
        with allure.step("Navigate to back from payment page"):
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
            self.select_element_is_clickable(self.locator.LINK_PDP_PEGE).click()

    def case_checking_pyment_info_and_back(self):
        with allure.step("Check text on info page "):
            word = self.select_element_is_visibile(self.locator.BACK_TO_PRODUCT_TEXT)
            self.check_word(word, "Back to products")
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/inventory-item.html?id=4")


    def checking_pyment_info_and_back_and_remove_item(self):
        with allure.step("Remove item in pyment page"):
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
            self.select_element_is_clickable(self.locator.LINK_PDP_PEGE).click()
            self.select_element_is_clickable(self.locator.REMOVE_BTN).click()

    def case_checking_pyment_info_and_back_and_remove(self):
        with allure.step("Check text, after remove item in payment page  "):
            word = self.select_element_is_visibile(self.locator.ADD_TO_CART)
            self.check_word(word,"Add to cart")
            self.get_current_url()


    def checking_pyment_info_and_back_and_back_to_cart(self):
        with allure.step("navigate to Cart in payment page"):
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
            self.select_element_is_clickable(self.locator.LINK_PDP_PEGE).click()
            self.select_element_is_clickable(self.locator.CART_ICON).click()

    def case_checking_pyment_info_and_back_and_back_to_cart(self):
        with allure.step("Check text in cart"):
            word = self.select_element_is_visibile(self.locator.YOUR_CART_BACK_INFO)
            self.check_word(word, "Your Cart")
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/cart.html")


    def checking_pyment_info_finish_order(self):
        with allure.step("Navigate to Finosh page"):
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


    def case_checking_info_finish_order(self):
        with allure.step("Check text on finosh page"):
            word = self.select_element_is_visibile(self.locator.THK_YOU_ORDER)
            self.check_word(word, "Thank you for your order!")
            self.get_current_url()
            self.equal_url("https://www.saucedemo.com/checkout-complete.html")
            self.take_scrn_shot()










