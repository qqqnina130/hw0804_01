from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time


class BNAL_Login:

    def __init__(self):
        # 启动参数
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1',
            'deviceName': 'sanxing',
            'appPackage': 'com.yunmall.lc',
            'appActivity': 'com.yunmall.ymctoc.ui.activity.MainActivity'
        }

        # 声明驱动
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    """每一个方法封装了一个业务操作"""
    # 显式等待
    def wait_ele(self, ty, val):
        """
        :param ty: 类型
        :param val: 属性值
        :return:返回元素定位对象
        """
        wd = WebDriverWait(self.driver, 5, 1)
        if ty == "id":
            return wd.until(lambda x: x.find_element_by_id(val))
        if ty == "class":
            return wd.until(lambda x: x.find_element_by_class_name(val))
        if ty == "xpath":
            return wd.until(lambda x: x.find_element_by_xpath(val))
    # 滑动屏幕
    def swipe_screen(self, tag=1):  # 默认向上滑动
        """
        滑动屏幕操作
        :param tag: 1:向上 2:向下 3:向左 4:向右
        :return:
        """
        # 分辨率
        size = self.driver.get_window_size()
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")
        # 等待
        time.sleep(2)

        # 方向滑动
        if tag == 1:
            # x(宽*50%), y(高 * 80 %) -> x(宽*50%), y(高 * 20 %)
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)
        if tag == 2:
            # x(宽*50%), y(高 * 20 %) -> x(宽*50%), y(高 * 80 %)
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 2000)
        if tag == 3:
            # x(宽*80%), y(高 * 50 %) -> x(宽*20%), y(高 * 50 %)
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)
        if tag == 4:
            # x(宽*20%), y(高 * 50 %) -> x(宽*80%), y(高 * 50 %)
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 2000)

    def close_update(self):
        # 关闭更新
        self.wait_ele("id", "com.yunmall.lc:id/img_close").click()

    def click_my_btn(self):
        """首页点击我"""
        # 点击我
        self.wait_ele("id", "com.yunmall.lc:id/tab_me").click()


    def login(self, name, pwd, exp):
        """
        登录
        :param name: 登录账号
        :param pwd: 登录密码
        :param exp: 用户名
        :return:
        """
        # 已有账号去登录
        self.wait_ele("id", "com.yunmall.lc:id/textView1").click()
        #
        # 用户名
        account = self.wait_ele("id", "com.yunmall.lc:id/logon_account_textview")
        account.clear()  # 输入前先清空
        account.send_keys(name)
        # 密码
        passwd = self.wait_ele("id", "com.yunmall.lc:id/logon_password_textview")
        passwd.clear()
        passwd.send_keys(pwd)
        # 登录按钮
        self.wait_ele("id", "com.yunmall.lc:id/logon_button").click()
        # 登录用户名
        user_name = self.wait_ele("id", "com.yunmall.lc:id/tv_user_nikename").text
        # 文本包含字符判断
        if exp in user_name:  # 有可能包含空格
            print("登陆成功")
        else:
            print("登陆失败")

    def logout(self):
        """退出"""
        # 点击设置
        self.wait_ele("id", "com.yunmall.lc:id/ymtitlebar_left_btn_image").click()
        # 滑动屏幕
        self.swipe_screen()
        # 点击退出
        self.wait_ele("id", "com.yunmall.lc:id/setting_logout").click()
        # 点击确认退出
        self.wait_ele("id", "com.yunmall.lc:id/ymdialog_right_button").click()

    def get_sign_text(self):
        """获取手机号注册按钮"""
        value = self.wait_ele("id", "com.yunmall.lc:id/register_button")
        if "手机号注册" in value.text:  # 有可能包含空格
            print("退出成功")
        else:
            print("退出失败")


if __name__ == '__main__':
    # 实例化类
    bn = BNAL_Login()
    # 关闭更新
    bn.close_update()
    # 点击我
    bn.click_my_btn()
    # 登录
    bn.login("13488834010", "159357li", "mlili")
    # 退出
    bn.logout()
    # 点击我
    bn.click_my_btn()
    # 验证是否退出成功
    bn.get_sign_text()

