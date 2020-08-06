import time

from selenium.webdriver.support.wait import WebDriverWait

from Base.driver import Driver


class Base:

    def __init__(self):
        # 赋值自定义声明driver
        self.driver = Driver.get_app_driver()

    def search_ele(self, loc, timeout=5, poll=1.0):
        """
        定位单个元素
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CSS,属性值)...
        :param timeout: 搜索元素超时时间
        :param poll: 搜索元素间隔时间
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def click_ele(self, loc, timeout=5, poll=1.0):
        """
        点击元素
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CSS,属性值)....
        :param timeout: 搜索元素超时时间
        :param poll: 搜索元素间隔时间
        :return:
        """
        self.search_ele(loc, timeout, poll).click()

    def send_ele(self, loc, text, timeout=5, poll=1.0):
        """
        输入框输入内容
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CSS,属性值)....
        :param text: 输入文本
        :param timeout: 搜索元素超时时间
        :param poll: 搜索元素间隔时间
        :return:
        """
        # 定位
        input_text = self.search_ele(loc, timeout, poll)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)

    def swipe_ele(self, tag=1): # 默认向上滑动
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
