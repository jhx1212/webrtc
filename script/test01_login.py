import time
import unittest


from base import init
from base.base_driver import DriverUtil
from page.login_page import LoginPage

# from base.assert_action import AssertAction

import sys
sys.setrecursionlimit(100000)

class Testlogin(unittest.TestCase):

    #初始化对象
    def setUp(self) -> None:
        self.driver=DriverUtil().get_driver()
        self.login_page=LoginPage(self.driver)

    # 关闭浏览器
    def tearDown(self) -> None:
        time.sleep(2)
        DriverUtil().quit_driver()

    # 登录(正确的用户名和密码)
    def test01_login_action(self):
        self.login_page.login_action()


    #  登录,  密码错误
    def test02_login_error(self):
        self.login_page.login_action_error01()

