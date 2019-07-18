import time

from base import init
from base.base_aciton import BaseAciton
from base.assert_action import AssertAction
from base.base_log import Log


#封装登录
class LoginPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)
        # self.web_driver_wait_acrion=WebDriverWaitAction()
        self.assert_action=AssertAction(self.driver)
        self.log=Log()


    # 每个功能都定义到函数里面  功能:点击登录logo
    def click_login_logo(self):
        self.click_element(init.login_logo)
    #输入用户名
    def input_username_text(self):
        self.click_element(init.login_username)
        self.input_element_content(init.login_username,init.login_page_username)
        time.sleep(2)
    # 输入密码
    def input_password_text(self):
        self.click_element(init.login_password)
        self.input_element_content(init.login_password,init.login_page_password)
        time.sleep(2)
    #点击登录按钮
    def click_login_button(self):
        self.click_element(init.login_button)
        time.sleep(2)
    # 定义一个登陆的完整操作,用户名和密码均有效,在单独测试其它功能时先调用此方法完成登陆
    def login_action(self):
        self.click_login_logo()
        time.sleep(1)
        self.input_username_text()
        time.sleep(1)
        self.input_password_text()
        self.click_login_button()

        # 断言
        login_assert_photo_error01 = "login_assert_error"
        rec=self.find_element(init.login_page_username_element).text
        # self.assert_action.assert_in(init.login_page_username,self.find_element(init.login_page_username_element).text, login_assert_photo_error01)
        self.assert_action.assert_in("座席分组："+init.login_page_username,rec,login_assert_photo_error01)
        # 输出日志login_success
        self.log.debug("login_ok")

    def login_action_error01(self):
        self.click_login_logo()
        time.sleep(1)
        self.input_username_text()
        time.sleep(1)
        # 输入错误的密码1111111
        self.click_element(init.login_password)
        self.input_element_content(init.login_password,"1111111")

        # 断言是否登录失败
        login_assert_photo_error02 = "login_assert_error_pw"
        self.assert_action.assert_in("未登录",self.find_element(init.login_page_error_element).text,login_assert_photo_error02)
        # print(self.find_element(init.login_page_error_element).text)






