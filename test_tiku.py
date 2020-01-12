# test_tiku.py
# coding:utf-8
import pytest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

WIDTH = 414  # 宽度
HEIGHT = 736  # 高度
PIXEL_RATIO = 5.0  # 分辨率
mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(options=options)


def setup_module():
    driver.get("http://www.kuaixuezaixian.com/i/login")  # 打开考呀呀登录页
    driver.implicitly_wait(30)


def teardown_module():
    time.sleep(2)
    driver.quit()


class TestCase:

    def test_kyy_nub_login(self):
        # 定位到账号输入框并获取输入的账号
        driver.find_element_by_tag_name("input").send_keys("15970670806")
        # 定位到密码输入框并获取输入的密码
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div[2]/form/div[2]/input").send_keys(
            "123456")
        driver.find_element_by_class_name("submit-btn").click()
        time.sleep(2)

    def test_kyy_learn(self):
        # 进入学习
        driver.find_element_by_xpath("//*[@id='app']/div[1]/footer/ul/li[3]/a").click()
        time.sleep(1)
        # 选择班级
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div[2]/div[1]/div[7]").click()
        # 关闭指示
        driver.find_element_by_xpath("/html/body/div[8]/div/div[5]/a").click()
        time.sleep(1)

    def test_kyy_tiku(self):
        # 进入全部题库
        driver.find_element_by_xpath("//*[@id='tiku']/div[1]/span").click()
        # 关闭提示
        driver.find_element_by_xpath("/html/body/div[8]/div/div[5]/a").click()
        time.sleep(1)

    def test_kyy_keeplearn(self):
        # 开始章节练习
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div[4]/div[2]/div[1]").click()
        # 进入第一章练习
        ac = driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div/div[2]/div")
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        driver.implicitly_wait(10)

    def test_kyy_practice(self):
        # 去除提示
        ac = driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[5]/div[2]/div/div[1]/img")
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        # 点击查看答案
        ac = driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[1]/div[4]/div/span[1]/img")
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        # 提交报错
        ac = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div[3]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/span")
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[1]/div[1]/div/div/div[2]/textarea").send_keys(
                                     "这是一个测试这是一个测试")
        driver.find_element_by_xpath("/html/body/div[6]/div/div[3]/button").click()
        time.sleep(1)


if __name__ == '__main__':
    pytest.main(["-s", "test_tiku.py"])
