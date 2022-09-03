from ..base_page import BasePage
from .pickup_page_locators import PickupPageLocators as Loc


class PickupPage(BasePage):
    def should_be_pickup_page(self):
        self.should_be_pickup_title()
        self.should_be_pickup_url()

    def should_be_pickup_url(self):
        assert "pickup" in self.browser.current_url, "This isn't pickup page"

    def should_be_pickup_title(self):
        assert "Самовывоз" in self.browser.find_element(*Loc.pickup_page_title).text, \
            "This page doesn't have pickup title"
