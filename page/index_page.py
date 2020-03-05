"""
首页页面
"""
import page
from base.base_page import BasePage


class IndexPage(BasePage):
    mine = page.mine

    def click_mine(self):
        self.click_func(self.mine)

