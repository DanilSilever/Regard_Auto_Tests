from selenium.webdriver.common.by import By


class MainPageLocators:
    about_link = (By.CSS_SELECTOR, ".Nav_link__1H5gx[href='/about']")
    delivery_link = (By.CSS_SELECTOR, ".Nav_link__1H5gx[href='/delivery']")
    pickup_link = (By.CSS_SELECTOR, ".Nav_link__1H5gx[href='/pickup']")
    warranty_link = (By.CSS_SELECTOR, ".Nav_link__1H5gx[href='/warranty']")
    contacts_link = (By.CSS_SELECTOR, ".Nav_link__1H5gx[href='/contacts']")
    search_input = (By.CSS_SELECTOR, "#searchInput")
    search_button = (By.CSS_SELECTOR, "[class*=Search_searchIcon]")
    profile_button = (By.CSS_SELECTOR, "[class*=IconButton_profile]")
    authorization_window = (By.CSS_SELECTOR, "#AUTHORIZATION_MODAL_WRAPPER")
    location_window = (By.CSS_SELECTOR, "#RECEIVE_TOWN_MODAL_WRAPPER")
    login_input = (By.CSS_SELECTOR, "input[name*=login]")
    password_input = (By.CSS_SELECTOR, "input[name*=password]")
    auth_button_submit = (By.CSS_SELECTOR, "[class*=Auth_btnEnter]")
    location_changer = (By.CSS_SELECTOR, "[class*=CityChooser_text]")
    location_input = (By.CSS_SELECTOR, "form>div>div[class*=Input_wrap]>input[class*=input]")

    @staticmethod
    def get_location_button_by_name(name):
        return By.CSS_SELECTOR, f"#townList>li[data-name={name}]"

