from ..base_page import BasePage
from .warranty_page_locators import WarrantyPageLocators as Loc


class WarrantyPage(BasePage):
    def should_be_warranty_page(self):
        self.should_be_warranty_title()
        self.should_be_warranty_url()

    def should_be_warranty_url(self):
        assert "warranty" in self.browser.current_url, "This isn't warranty page"

    def should_be_warranty_title(self):
        assert "Гарантия" in self.browser.find_element(*Loc.warranty_page_title).text, \
            "This page doesn't have warranty title"
