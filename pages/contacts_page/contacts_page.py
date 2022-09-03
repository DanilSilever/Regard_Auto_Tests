from ..base_page import BasePage
from .contacts_page_locators import ContactsPageLocators as Loc
import time


class ContactsPage(BasePage):
    def should_be_contacts_page(self):
        self.should_be_contacts_titles()
        self.should_be_contacts_url()

    def should_be_contacts_url(self):
        cur_url = self.browser.current_url
        assert "contacts" in cur_url, "This isn't contacts page"

    def should_be_contacts_titles(self):
        page_titles = self.browser.find_elements(*Loc.contacts_page_titles)
        assert "Интернет - магазин" in page_titles[0].text, "This page doesn't have online-store information"
        assert "Пункт выдачи Регард" in page_titles[1].text, "This page doesn't have pickup information"
        assert "Гарантийный отдел" in page_titles[2].text, "This page doesn't have warranty information"
