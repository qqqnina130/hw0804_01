from appium import webdriver


class Driver:
    """
        1.可以声明和退出app驱动
        2.可以声明和退出web驱动
    """

    # app驱动
    __app_driver = None

    @classmethod  # 不实例化类也可以直接调用该方法：类名.方法名（）
    def get_app_driver(cls):
        # 声明app驱动
        if cls.__app_driver is None:
            # __app_driver赋值
            # 启动参数
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.yunmall.lc',
                'appActivity': 'com.yunmall.ymctoc.ui.activity.MainActivity'
            }

            # 声明驱动
            cls.__app_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            # 返回driver
            return cls.__app_driver
        else:
            # __app_driver已经赋值
            return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        # 退出app driver
        if cls.__app_driver:
            # 如果__app_driver有值
            cls.__app_driver.quit()
            # 执行完quit方法后，__app_driver的值也不是None
            cls.__app_driver = None


# if __name__ == '__main__':
#     Driver.get_app_driver()
#     Driver.quit_app_driver()
#
