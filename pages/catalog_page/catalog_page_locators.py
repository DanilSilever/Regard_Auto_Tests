from selenium.webdriver.common.by import By


class CatalogPageLocators:
    products_title = (By.CSS_SELECTOR, "div[class*=CardText_listing]>a>h6")
    search_message = (By.CSS_SELECTOR, "div[class*=FilterTags_item]")
