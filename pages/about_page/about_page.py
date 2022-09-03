from ..base_page import BasePage
from .about_page_locators import AboutPageLocators as Loc


class AboutPage(BasePage):
    def should_be_about_page(self):
        self.should_be_about_title()
        self.should_be_about_url()

    def should_be_about_url(self):
        assert "about" in self.browser.current_url, "This isn't about page"

    def should_be_about_title(self):
        assert "О компании" == self.browser.find_element(*Loc.about_header).text, "This page doesn't have about title"

