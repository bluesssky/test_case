# test_home.py
# coding:utf-8

import pytest
import time
from selenium.webdriver import ActionChains
from selenium import webdriver

WIDTH = 414  # 宽度
HEIGHT = 736  # 高度
PIXEL_RATIO = 5.0  # 分辨率
mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(options=options)
# driver.get("http://www.kaoyaya.com/i")  # 打开考呀呀首页
driver.implicitly_wait(30)


def setup_module():
    # 打开考呀呀登录页
    driver.get("http://www.kaoyaya.com/i/login?returnurl=http%3A%2F%2Fwww.kaoyaya.com%2Fi%2Fuser")
    driver.implicitly_wait(30)
    # 输入账号密码登入
    # username = int(input("请输入用户名/手机号："))
    # password = str(input("请输入密码："))
    # 定位到账号输入框并获取输入的账号
    driver.find_element_by_tag_name("input").send_keys("15207058460")
    # 定位到密码输入框并获取输入的密码
    driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div[2]/form/div[2]/input").send_keys("123456")
    driver.find_element_by_class_name("submit-btn").click()


def teardown_module():
    time.sleep(2)
    driver.quit()




if __name__ == '__main__':
        pytest.main(["-s", "test_home.py"])