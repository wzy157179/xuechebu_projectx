"""
我的页面
"""
import page
from base.base_page import BasePage


class MinePage(BasePage):
    login = page.login  # 登录/注册
    nick_name = page.nick_name  # 用户名

    def click_login(self):
        """点击登录"""
        self.click_func(self.login)

    def get_nick_name(self):
        return self.find_element_func(self.nick_name).text
