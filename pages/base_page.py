from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by_method, selector):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((by_method, selector))
            )
        except TimeoutException:
            return False
        return True

    def is_element_not_present(self, by_method, selector):
        try:
            WebDriverWait(self.browser, 5).until_not(
                EC.presence_of_element_located((by_method, selector))
            )
        except TimeoutException:
            return False
        return True

    def is_element_clickable(self, by_method, selector):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((by_method, selector))
            )
        except TimeoutException:
            return False
        return True

    def is_url_contains(self, url_fragment):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.url_contains(url_fragment)
            )
        except TimeoutException:
            return False
        return True
