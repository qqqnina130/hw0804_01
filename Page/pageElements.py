from selenium.webdriver.common.by import By

class PageElements:
    """管理所有页面元素"""

    # ---搜索页面类---
    # 首页
    # 关闭更新按钮
    close_update_btn = (By.ID, "com.yunmall.lc:id/img_close")
    # ‘我’按钮
    my_btn = (By.ID, "com.yunmall.lc:id/tab_me")

    # 去登录 页面
    # 已有账号去登录 按钮
    go_to_btn = (By.ID, "com.yunmall.lc:id/textView1")

    # 登录页面
    # 账号 输入框
    name_input = (By.ID, "com.yunmall.lc:id/logon_account_textview")
    # 密码 输入框
    psw_input = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    # 登录按钮
    login_btn = (By.ID, "com.yunmall.lc:id/logon_button")

    # 我的页面（已登录）
    # 显示用户名
    show_name = (By.ID, "com.yunmall.lc:id/tv_user_nikename")
    # 设置按钮
    setting_btn = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    # 设置页面-登出
    # 退出按钮
    log_out_btn = (By.ID, "com.yunmall.lc:id/setting_logout")
    # 确认退出按钮
    log_out_confirm_btn = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")

