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


# 验证品类选择
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


# 验证消息中心
class TestCase_Home_Msg:
    def test_msg(self):
        # 进入消息中心
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/span/i").click()
        ac = driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/div[2]/div/div/div[2]")
        ActionChains(driver).move_to_element(ac).click(ac).perform()  # 通知
        bc = driver.find_element_by_class_name("back")
        ActionChains(driver).move_to_element(bc).click(bc).perform()  # 返回首页


# 验证banner图
class TestCase_Home_Banner:
    def test_banner(self):
        # 随机点击banner图
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/div/div[4]/img").click()
        driver.back()  # 返回首页
        # time.sleep(4)   # 暂时不能实现
        # # 等待banner图轮换后再次点击
        # driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/div/div[4]/img").click()
        # driver.back()  # 返回首页


# 验证金刚区
class TestCase_Home_ExamSelect:
    def test_select_list(self):
        # 选择精选好课
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[3]/div/span[1]/div").click()
        time.sleep(1)
        driver.back()
        # 选择每日一练
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[3]/div/span[2]/div").click()
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div[2]/div/div").click()  # 进入挑战
        time.sleep(1)
        driver.back()
        driver.find_element_by_class_name("toggle").click()  # 展开日历
        time.sleep(1)
        driver.find_element_by_class_name("toggle").click()  # 再次点击收起
        driver.find_element_by_class_name("back").click()
        # 选择考试资讯
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[3]/div/span[3]").click()
        time.sleep(2)
        driver.back()
        # 选择在线咨询
        driver.find_element_by_id('zhiCustomBtn').click()
        time.sleep(3)
        driver.refresh()


class TestCase_Resource:
    # 精品体验课
    def test_free_course(self):
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[5]/div[2]/div/div/div[1]/div/div[1]").click()
        time.sleep(0.5)
        driver.back()
        # 相对于顶部向下拖动10000个元素   实现不了
        # js = "var q=document.documentElement.scrollTop=10000"
        # driver.execute_script(js)
        # time.sleep(3)

        # 向下拖动到某一元素置顶，可以实现，这里是拖动到智能题库置顶
        target = driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[5]/div[4]/h5")
        driver.execute_script("arguments[0].scrollIntoView();", target)

    # 智能题库
    def test_tiku_section(self):
        ac = driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[5]/div[4]/div/div/div/div[1]")
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        time.sleep(0.5)
        driver.back()

    # 名师推荐
    def test_teacher_recommend(self):
        ac = driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[5]/div[6]/div/div[1]")
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        time.sleep(0.5)
        driver.back()

        target = driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[5]/div[6]/a/div")
        driver.execute_script("arguments[0].scrollIntoView();", target)
        bc = driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[5]/div[6]/a/div/i[2]")
        ActionChains(driver).move_to_element(bc).click(bc).perform()
        time.sleep(0.5)
        driver.back()

        # 移动到名师直播置顶
        target = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[5]/div[7]/div[1]")
        driver.execute_script("arguments[0].scrollIntoView();", target)

    # 名师直播
    def test_teacher_living(self):
        ac = driver.find_element_by_class_name("broadcast-content")
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        time.sleep(0.5)
        driver.back()


# 进入首页继续学习
class TestCase_KeepLearn:
    def test_keep_learn(self):
        ac = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[4]/div[2]/div[2]")
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        time.sleep(1)
        driver.back()


if __name__ == '__main__':
        pytest.main(["-s", "test_home.py"])

