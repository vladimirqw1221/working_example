import pytest
import  allure
from pages.critical_patch import CriticallPatchClass


class TestCriticalParch:
    @pytest.fixture
    def set_up(self,driver):
        set_up = CriticallPatchClass(driver, "https://www.saucedemo.com/")
        set_up.open_browser()
        return set_up

    @pytest.mark.usefixtures("driver")
    @allure.title("Critical patch for register user")
    @allure.feature("Critical patch")
    @allure.tag("Critical patch")
    def test_critical_path_for_register_user(self, set_up):
        set_up.criticall_patch_for_register_user()
        set_up.case_criticall_patch_for_register_user()

    @pytest.mark.usefixtures("driver")
    @allure.title("Critical patch for user guest")
    @allure.feature("Critical patch")
    @allure.tag("Critical patch")
    def test_criticall_patch_for_guest_user(self, set_up):
        set_up.criticall_patch_for_guest_user()
        set_up.case_criticall_patch_for_guest_user()


