import time

from ..base_page import BasePage
from ..about_page.about_page import AboutPage
from ..delivery_page.delivery_page import DeliveryPage
from ..pickup_page.pickup_page import PickupPage
from ..warranty_page.warranty_page import WarrantyPage
from ..contacts_page.contacts_page import ContactsPage
from ..catalog_page.catalog_page import CatalogPage
from ..profile_page.profile_page import ProfilePage
from .main_page_locators import MainPageLocators as Loc
from ui_utils.main_user import MainUser


class MainPage(BasePage):

    def go_to_about_page(self):
        self.browser.find_element(*Loc.about_link).click()
        return AboutPage(self.browser, self.browser.current_url)

    def go_to_delivery_page(self):
        self.browser.find_element(*Loc.delivery_link).click()
        return DeliveryPage(self.browser, self.browser.current_url)

    def go_to_pickup_page(self):
        self.browser.find_element(*Loc.pickup_link).click()
        return PickupPage(self.browser, self.browser.current_url)

    def go_to_warranty_page(self):
        self.browser.find_element(*Loc.warranty_link).click()
        return WarrantyPage(self.browser, self.browser.current_url)

    def go_to_contacts_page(self):
        self.browser.find_element(*Loc.contacts_link).click()
        return ContactsPage(self.browser, self.browser.current_url)

    def search_product(self, product_name):
        search_area = self.browser.find_element(*Loc.search_input)
        search_area.send_keys(product_name)
        if self.is_element_clickable(*Loc.search_button):
            self.browser.find_element(*Loc.search_button).click()
        if self.is_url_contains("catalog"):
            catalog_page = CatalogPage(self.browser, self.browser.current_url)
            catalog_page.should_be_inserted_product(product_name)

    def login(self):
        self.browser.find_element(*Loc.profile_button).click()
        self.is_element_present(*Loc.authorization_window)
        self.browser.find_element(*Loc.login_input).send_keys(MainUser.email)
        self.browser.find_element(*Loc.password_input).send_keys(MainUser.pswd)
        self.browser.find_element(*Loc.auth_button_submit).click()

        # go to profile page after authorization
        self.is_element_not_present(*Loc.authorization_window)
        self.browser.find_element(*Loc.profile_button).click()
        profile_page = ProfilePage(self.browser, self.browser.current_url)
        profile_page.should_be_users_profile(MainUser.email)

    def switch_location(self, exp_location_name):
        self.browser.find_element(*Loc.location_changer).click()
        self.is_element_present(*Loc.location_window)
        self.browser.find_element(*Loc.location_input).send_keys(exp_location_name)
        self.browser.find_element(*Loc.get_location_button_by_name(exp_location_name)).click()

        self.is_element_not_present(*Loc.location_window)
        location_name = self.browser.find_element(*Loc.location_changer).text
        assert location_name == exp_location_name, f"Expected {exp_location_name}, got {location_name}"

