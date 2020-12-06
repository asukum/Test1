from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    #  Object Repository of Login Page
    HOME_USERS_BUTTON = (By.XPATH, "//a[@href='/users/auth/dexcom_sts']")
    HEALTHCARE_USERS_BUTTON = (By.XPATH, "//a[@href='/clinic?locale=en-US']")
    HOME_USERS_USERNAME = (By.NAME, "username")
    HOME_USERS_PASSWORD = (By.NAME, "password")
    HOME_USERS_LOGIN_BUTTON = (By.NAME, "op")

    #  Constructor of LoginPage Class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    #  Actions of Login Page

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_healthcheck_user_link_exist(self):
        return self.is_visible(self.HEALTHCARE_USERS_BUTTON)

    def is_home_user_link_exist(self):
        return self.is_visible(self.HOME_USERS_BUTTON)

    def select_user_type(self, usertype):
        if usertype == "home":
            self.do_click(self.HOME_USERS_BUTTON)

        if usertype == "healthcare":
            self.do_click(self.HEALTHCARE_USERS_BUTTON)

    def do_login(self, username, password):
        self.do_send_keys(self.HOME_USERS_USERNAME, username)
        self.do_send_keys(self.HOME_USERS_PASSWORD, password)
        self.do_click(self.HOME_USERS_LOGIN_BUTTON)

