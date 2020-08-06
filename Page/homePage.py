# import time

from selenium.webdriver.common.by import By
from Base.Base import Base
from Page.pageElements import PageElements


class HomePage(Base):

    def __init__(self):
        super().__init__()


    def close_update(self):
        """点击 关闭更新按钮"""
        self.click_ele(PageElements.close_update_btn)

    def click_my_btn(self):
        """点击 '我'"""
        self.click_ele(PageElements.my_btn)


# if __name__ == '__main__':
#     Driver.get_app_driver()
#     homepage = HomePage()
#     homepage.close_update()
#     homepage.click_my_btn()
#     time.sleep(2)
#     Driver.quit_app_driver()


