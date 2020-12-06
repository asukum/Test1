import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Utils.Logging.logging import logBase


class Test_Login(BaseTest, logBase):

    def test_healthcheck_user_link_exist(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_healthcheck_user_link_exist()
        assert flag

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.select_user_type("home")
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
