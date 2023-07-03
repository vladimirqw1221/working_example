import pytest

from pages.problem_user import ProblemUserClass


class TestProblemUser:
    @pytest.fixture
    def set_up(self,driver):
        set_up = ProblemUserClass(driver, "https://www.saucedemo.com/")
        set_up.open_browser()
        return set_up

    def test_problem_user(self, set_up):
        set_up.problem_user()
        set_up.case_check_button()

    def test_ptodlem_user_add_to_cart_all_item(self, set_up):
        set_up.addet_all_item()
        set_up.checking_cart_case()

    def test_check_order_problem_user(self, set_up):
        set_up.check_order_for_problem_user()
        set_up.case_for_problem_user()

