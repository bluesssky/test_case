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
    driver.find_element_by_tag_name("input").send_keys("18879958433")
    # 定位到密码输入框并获取输入的密码
    driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div[2]/form/div[2]/input").send_keys("123456")
    driver.find_element_by_class_name("submit-btn").click()
    # driver.implicitly_wait(30)


class TestCase_Home_Class:
    def test_class_type1(self):
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/footer/ul/li[1]/a").click()   # 点击进入首页
        ac = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[1]/span")   # 选择分类
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        # time.sleep(1)

    def test_class_type2(self):
        ac = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]")  # 选择中级分类
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        # time.sleep(1)

    def test_class_type4(self):
        ac = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[1]/span")  # 选择分类
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        time.sleep(1)
        ac = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[4]")  # 选择管会
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        # time.sleep(1)

    def test_class_return_type1(self):
        bc = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[1]/span")  # 选择分类
        ActionChains(driver).move_to_element(bc).click(bc).perform()
        # time.sleep(1)
        ac = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]")  # 选择初级
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        # time.sleep(1)


class TestCase_Home_Msg:
    def test_msg(self):
        # 进入消息中心
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/span/i").click()
        ac = driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/div[2]/div/div/div[2]")
        ActionChains(driver).move_to_element(ac).click(ac).perform()  # 通知
        bc = driver.find_element_by_class_name("back")
        ActionChains(driver).move_to_element(bc).click(bc).perform()  # 返回首页


def teardown_module():
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
        pytest.main(["-s", "test_home.py"])

