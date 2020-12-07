import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Utils.Logging.logging import logBase


class Test_Login(BaseTest, logBase):
    # Test case to check whether the health Care User Login link exist
    def test_healthcare_user_link_exist(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_healthcare_user_link_exist()
        assert flag

    # Test case to check whether the Home User Login link exist
    def test_home_user_link_exist(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_home_user_link_exist()
        assert flag

    # Test case to Select Home User and Login
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.select_user_type("home")
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
