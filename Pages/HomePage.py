from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    # Object Repository of Home Page

    #  Constructor of HomePage Class
    def __init__(self, driver):
        super().__init__(driver)

    #  Actions of Home Page

    def get_home_page_title(self, title):
        return self.get_title(title)
