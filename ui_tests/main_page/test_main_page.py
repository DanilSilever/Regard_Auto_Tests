import pytest
import allure
from pages.main_page.main_page import MainPage


@pytest.mark.main_page
class TestMainPage:
    link = "https://www.regard.ru/"

    @allure.title("Switch between main pages")
    @pytest.mark.parametrize('case', [
        "about",
        "delivery",
        "pickup",
        "warranty",
        "contacts"
    ])
    def test_switch_between_main_pages(self, browser, case):
        page = MainPage(browser, self.link)
        page.open()

        match case:
            case "about":
                about_page = page.go_to_about_page()
                about_page.should_be_about_page()
            case "delivery":
                delivery_page = page.go_to_delivery_page()
                delivery_page.should_be_delivery_page()
            case "pickup":
                pickup_page = page.go_to_pickup_page()
                pickup_page.should_be_pickup_page()
            case "warranty":
                warranty_page = page.go_to_warranty_page()
                warranty_page.should_be_warranty_page()
            case "contacts":
                contacts_page = page.go_to_contacts_page()
                contacts_page.should_be_contacts_page()

    @allure.title("Search product")
    def test_product_search(self, browser):
        page = MainPage(browser, self.link)
        page.open()

        product = "RTX 3070 Ti VENTUS 3X 8G OC"
        page.search_product(product)

    @allure.title("Test login")
    def test_login_main_page(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.login()

    @allure.title("Switch location")
    @pytest.mark.parametrize('location', [
        "Пятигорск",
        pytest.param("True", marks=pytest.mark.xfail)
    ])
    def test_switch_location(self, browser, location):
        page = MainPage(browser, self.link)
        page.open()
        page.switch_location(location)
