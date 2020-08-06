import time

from selenium.webdriver.common.by import By
from Base.Base import Base
from Base.driver import Driver
from Page.gotoPage import GotoPage
from Page.homePage import HomePage
from Page.loginPage import LoginPage
from Page.pageElements import PageElements


class LogoutPage(Base):

    def __init__(self):
        super().__init__()


    def upward_swipe(self):
        """向上滑动"""
        self.swipe_ele()

    def click_logout(self):
        """点击退出按钮"""
        self.click_ele(PageElements.log_out_btn)

    def click_logout_confirm(self):
        """点击确认退出按钮"""
        self.click_ele(PageElements.log_out_confirm_btn)


# if __name__ == '__main__':
#     Driver.get_app_driver()
#     homepage = HomePage()
#     gotopage = GotoPage()
#     loginpage = LoginPage()
#     mypage = MyPage()
#
#     homepage.close_update()
#     homepage.click_my_btn()
#     time.sleep(2)
#     gotopage.go_to_login()
#     time.sleep(2)
#     loginpage.name_input_text("18721576647")
#     loginpage.psw_input_text("ssalin130")
#     loginpage.log_in()
#     time.sleep(2)
#
#     Driver.quit_app_driver()
