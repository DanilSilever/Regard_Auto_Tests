from ..base_page import BasePage
from .catalog_page_locators import CatalogPageLocators as Loc


class CatalogPage(BasePage):
    def should_be_inserted_product(self, inserted_name):
        self.check_inserted_product_in_search_message(inserted_name)
        products_title = self.browser.find_element(*Loc.products_title).text
        assert inserted_name in products_title, f"Expected {inserted_name} in title, but got {products_title}"

    def check_inserted_product_in_search_message(self, inserted_name):
        search_message = self.browser.find_element(*Loc.search_message).text
        assert inserted_name == search_message, f"Expected {inserted_name}, but got {search_message}"
