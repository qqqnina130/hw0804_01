from Base.driver import Driver
import pytest

from Page.gotoPage import GotoPage
from Page.homePage import HomePage
from Page.loginPage import LoginPage
from Page.logoutPage import LogoutPage
from Page.myPage import MyPage


class TestLogin:

    def setup_class(self):
        # 实例化页面类
        self.home_page = HomePage()
        self.goto_page = GotoPage()
        self.login_page = LoginPage()
        self.my_page = MyPage()
        self.logout_page = LogoutPage()

        # 关闭更新
        self.home_page.close_update()


    def teardown_class(self):
        # # 点击 设置按钮
        # self.my_page.click_setting()
        # # 向上滑动
        # self.logout_page.upward_swipe()
        # # 点击 退出按钮
        # self.logout_page.click_logout()
        # # 点击 确认退出按钮
        # self.logout_page.click_logout_confirm()
        """退出驱动"""
        Driver.quit_app_driver()

    def setup(self):
        try:
            # 登陆账号 #登录失败时，此代码报错 执行下列代码
            # 点击‘我’
            self.home_page.click_my_btn()
            # 点击 已有账号去登录
            self.goto_page.go_to_login()
        except:
            pass

    # 添加数据
    @pytest.mark.parametrize("name_data, psw_data, name_result", [("18721576647", "ssalin130", "Nina0130"),(" 18721576647", "ssalin130", "Nina0130"), ("18721576647 ", "ssalin130", "Nina0130")])
    # (" 18721576647", "ssalin130", "Nina0130"), ("18721576647 ", "ssalin130", "Nina0130")
    def test_login_data(self, name_data, psw_data, name_result):
        """
        输入 账号、密码 和 判断用户名是否正确
        :param name_data: 账号
        :param psw_data: 密码
        :param name_result: 预期显示用户名
        :return:
        """
        self.login_page.name_input_text(name_data)
        self.login_page.psw_input_text(psw_data)
        self.login_page.log_in()

        assert self.my_page.name_result_text() == name_result



# if __name__ == '__main__':
#     Driver.get_app_driver()
#     Driver.quit_app_driver()

