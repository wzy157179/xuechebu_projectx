"""
登录测试用例
"""
import time

import pytest

from page.page_factory import PageFactory
from utils import get_driver


class TestLogin(object):
    """登录测试类"""

    @pytest.fixture()
    def before_func(self):
        self.driver = get_driver()
        self.page_factory = PageFactory(self.driver)
        yield
        time.sleep(2)
        self.driver.quit()

    def test_login(self, before_func):
        """登录测试方式"""
        self.page_factory.index_page().click_mine()
        self.page_factory.mine_page().click_login()
        self.page_factory.login_page().input_phone('13614603168')
        self.page_factory.login_page().input_pwd('123456')
        self.page_factory.login_page().click_login_btn()
        self.page_factory.login_page().click_confirm_btn()
        name = self.page_factory.mine_page().get_nick_name()
        assert "1621" in name
