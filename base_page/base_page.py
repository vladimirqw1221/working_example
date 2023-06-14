import time

import allure
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from enams.glodal_enams import GlobalEnums


class BaseClass:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_browser(self):
        self.driver.get(self.url)
        print("Open the browser")

    """ Method for selected element, on webpage and driver wait element"""

    def select_element_is_visibile(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def select_element_all_visibile(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def select_element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def select_element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def select_element_all_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def switch_on_frome(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def select_element_is_selected(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_selected(locator))

    def switc_to_new_window(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.new_window_is_opened(locator))

    """Method for selected element on webpage with help JavaScript sytax"""

    def remove_element_by_id(self, element):
        return self.driver.execute_script(f"document.getElementById{element}.remove();")

    def remove_element_by_class(self, element):
        return self.driver.execute_script(f"document.getElementByClassName{element}.remove();")

    def click_element_by_id(self, element):
        return self.driver.execute_script(f"document.getElementById{element}.click();")

    def click_element_by_class(self, element):
        return self.driver.execute_script(f"document.getElementByClassName{element}.click();")

    def scroll_to_element(self, element):
        return self.driver.execute_script("argument[0].scrollViewTo;", element)

    """Method for asset word on webpage"""

    def check_word(self, word, result):
        value_word = word.text
        assert value_word == result, GlobalEnums.WRONG_ERROR_WORD.value
        print("Test assert word passed")

    """Method for getting current url"""

    def get_current_url(self):
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")

    """Method for equal URL"""

    def equal_url(self, result):
        value_equal = self.driver.current_url
        assert value_equal == result, GlobalEnums.WRONG_ERROR_URL.value
        print(f"equal URL passed : {value_equal}")


    """Method for getting screenshot"""
    def take_scrn_shot(self):
        path_scrn = f'scr/screenshot{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png'
        screenshot = self.driver.get_screenshot_as_png()
        with open(path_scrn, "wb") as file:
            file.write(screenshot)
        allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
        print("Screenshot added")

    """Method for button back"""
    def navigate_to_back(self):
       self. driver.back()
       current_url_back = self.driver.current_url
       print(f"Navigate to back page  : {current_url_back}")
       return current_url_back



