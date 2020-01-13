# test_login.py
# coding:utf-8
import pytest
from selenium import webdriver
import time


WIDTH = 414  # 宽度
HEIGHT = 736  # 高度
PIXEL_RATIO = 5.0  # 分辨率
mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(options=options)


def setup_module():
    driver.get('http://www.kaoyaya.com/i/login')  # 打开考呀呀登录页
    driver.implicitly_wait(30)


def teardown_module():
    time.sleep(2)
    # driver.quit()


class TestCase:

    def test_kyy_nub_login(self):
        # 输入账号密码登入
        username = int(input("请输入用户名/手机号："))
        password = str(input("请输入密码："))
        # 定位到账号输入框并获取输入的账号
        # driver.find_element_by_tag_name("input").send_keys("15970670806")
        # # 定位到密码输入框并获取输入的密码
        # driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div[2]/form/div[2]/input").send_keys(
        #     "lt123456")
        # driver.find_element_by_class_name("submit-btn").click()
        driver.implicitly_wait(30)

    def test_kyy_login_exit(self):
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[2]/a[3]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div/button").click()
        time.sleep(1)

    # def kyy_login_phone(self):
    #     # 通过手机验证码登录
    #     driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[2]/p").click()
    #     driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/form/div[4]/span[1]").click()
    #     driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div[2]/form/div[4]/span[1]").click()
    #     mobile = int(input("请输入您绑定的手机号码："))
    #     # 定位到手机号输入框并获取输入手机号
    #     driver.find_element_by_tag_name("input").send_keys(mobile)
    #     # 发送验证码
    #     driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div[2]/form/div[2]/span/span").click()
    #     time.sleep(0.5)
    #     mobileCode = int(input("请输入验证码："))
    #     # 输入获取的验证码
    #     driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div[2]/form/div[2]/input").send_keys(mobileCode)
    #     driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div[2]/form/div[3]/div[1]/span").click()


if __name__ == '__main__':
    pytest.main(["-p", "test_login.py"])
