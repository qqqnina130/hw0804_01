import time

from selenium.webdriver.common.by import By
from Base.Base import Base
from Base.driver import Driver
from Page.gotoPage import GotoPage
from Page.homePage import HomePage
from Page.pageElements import PageElements


class LoginPage(Base):

    def __init__(self):
        super().__init__()


    def name_input_text(self, text):
        """输入账号"""
        self.send_ele(PageElements.name_input, text)

    def psw_input_text(self, text):
        """输入密码"""
        self.send_ele(PageElements.psw_input, text)

    def log_in(self):
        """点击登录按钮"""
        self.click_ele(PageElements.login_btn)


# if __name__ == '__main__':
#     Driver.get_app_driver()
#     homepage = HomePage()
#     gotopage = GotoPage()
#     loginpage = LoginPage()
#     homepage.close_update()
#     homepage.click_my_btn()
#     time.sleep(2)
#     gotopage.go_to_login()
#     time.sleep(2)
#     loginpage.name_input_text("18721576647")
#     loginpage.psw_input_text("ssalin130")
#     loginpage.log_in()
#     time.sleep(2)
#     Driver.quit_app_driver()
