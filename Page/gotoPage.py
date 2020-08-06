import time
from selenium.webdriver.common.by import By
from Base.Base import Base
# from Page.homePage import HomePage
from Page.pageElements import PageElements


class GotoPage(Base):

    def __init__(self):
        super().__init__()


    def go_to_login(self):
        """点击 已有帐号去登录"""
        self.click_ele(PageElements.go_to_btn)


# if __name__ == '__main__':
#     homepage = HomePage()
#     gotopage = GotoPage()
#     homepage.close_update()
#     homepage.click_my_btn()
#     time.sleep(2)
#     gotopage.go_to_login()
#     time.sleep(2)

