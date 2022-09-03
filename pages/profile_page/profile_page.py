from ..base_page import BasePage
from .profile_page_locators import ProfilePageLocators as Loc


class ProfilePage(BasePage):
    def should_be_users_profile(self, exp_email):
        users_email = self.browser.find_element(*Loc.profile_email).text
        self.should_be_profile_url()
        assert users_email == exp_email, f"Expected {exp_email} in url, but got {users_email}"

    def should_be_profile_url(self):
        assert self.is_url_contains("profile"), f"Expected 'profile' in url, but got {self.browser.current_url}"
