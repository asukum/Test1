from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Utils.Logging.logging import logBase


class Test_Home(BaseTest, logBase):

    # Test case to check the Homepage Title
    def test_homepage_title(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.select_user_type("home")
        homepage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        title = homepage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE



