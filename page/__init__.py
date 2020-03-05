"""
页面元素属性封装
"""
from selenium.webdriver.common.by import By

# 首页页面

mine = By.XPATH, '//*[contains(@text,"我的")]'  # 我的

# 我的页面

login = By.XPATH, '//*[contains(@text,"登录")]'  # 登录/注册

# 登陆页面

phone = By.ID, 'com.bjcsxq.chat.carfriend:id/login_phone_et'  # 账号
pwd = By.ID, 'com.bjcsxq.chat.carfriend:id/login_pwd_et'  # 密码
login_btn = By.ID, 'com.bjcsxq.chat.carfriend:id/login_btn'  # 登录按钮
comfirm_btn_ = By.ID, 'com.bjcsxq.chat.carfriend:id/btn_neg'  # 确定按钮
