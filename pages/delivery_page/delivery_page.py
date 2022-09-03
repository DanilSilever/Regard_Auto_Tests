from ..base_page import BasePage
from .delivery_page_locators import DeliveryPageLocators as Loc


class DeliveryPage(BasePage):
    def should_be_delivery_page(self):
        self.should_be_delivery_title()
        self.should_be_delivery_url()

    def should_be_delivery_url(self):
        assert "delivery" in self.browser.current_url, "This isn't delivery page"

    def should_be_delivery_title(self):
        assert "Доставка" in self.browser.find_element(*Loc.delivery_page_title).text, \
            "This page doesn't have delivery title"

