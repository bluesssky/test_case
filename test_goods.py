# test_home.py
# coding:utf-8

import pytest
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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


# 检查商城-全部
class TestCase_AllGoods:
    # 精选好课
    def test_good_goods(self):
        ac = driver.find_element_by_xpath("//*[@id='app']/div[1]/footer/ul/li[2]/a")
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        time.sleep(1)
        bc = driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[2]/div[2]/div/div[1]/div[1]")
        ActionChains(driver).move_to_element(bc).click(bc).perform()   # 精选好课
        time.sleep(0.5)
        # driver.find_element_by_id("tab-menu").click()  # 目录
        # time.sleep(0.5)
        # driver.find_element_by_id("tab-about").click()  # 介绍
        # driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[6]/div[1]/div[1]").click()  # 左下商城
        # time.sleep(1)
        # driver.back()
        # driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[6]/div[1]/div[2]").click()  # 客服
        # time.sleep(1)
        # driver.refresh()

    def test_buy_goods(self):
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[6]/div[2]").click()  # 购买
        time.sleep(0.5)
        # driver.find_element_by_class_name("popup-close").click()
        # time.sleep(0.5)
        # driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[6]/div[2]").click()
        # time.sleep(0.5)
        ac = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/button")
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        time.sleep(0.5)
        driver.find_element_by_class_name("address-item").click()  # 编辑地址
        time.sleep(0.5)
        # time.sleep(0.5)
        # bc = driver.find_element_by_class_name("name").click()
        # ActionChains(bc).key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
        # time.sleep(2)
        # driver.find_element_by_id("name").send_keys("坤亮")  # 收货人
        # driver.find_element_by_id("mobile").clear()
        # driver.find_element_by_id("mobile").send_keys("15207058460")  # 电话号
        # driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/ul/li[4]/div[2]/div/div[2]/textarea").clear()
        # driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/ul/li[4]/div[2]/div/div[2]/textarea").send_keys("朝阳区")  # 地址
        # time.sleep(0.5)
        # driver.find_element_by_class_name("edit-end").click()  # 保存
        driver.back()
        driver.find_element_by_class_name("order-button").click()  # 支付
        time.sleep(1)
        driver.get("https://www.kaoyaya.com/i/goodsStore")  # 回到商城首页


if __name__ == '__main__':
        pytest.main(["-s", "test_home.py"])
