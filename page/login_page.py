"""
登录页面
"""
import page
from base.base_page import BasePage


class LoginPage(BasePage):
    phone = page.phone  # 账号
    pwd = page.pwd  # 密码
    login_btn = page.login_btn  # 登录按钮
    confirm_btn = page.comfirm_btn  # 确定按钮

    def input_phone(self, phone):
        """输入账号"""
        self.input_func(self.phone, phone)

    def input_pwd(self, pwd):
        """输入密码"""
        self.input_func(self.pwd, pwd)

    def click_login_btn(self):
        """点击登录按钮"""
        self.click_func(self.login_btn)

    def click_confirm_btn(self):
        """点击确认按钮"""
        self.click_func(self.confirm_btn)
