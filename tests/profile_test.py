import random
import pytest
import allure

from base.base_test import BaseTest

@allure.feature("Profile Functionality")
class TestProfile(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_name(f"Test{random.randint(1,100)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()
