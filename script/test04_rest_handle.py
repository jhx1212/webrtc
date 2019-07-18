import time
import unittest



from base.base_driver import DriverUtil
from page.rest_handle import RestHandlePage
from page.login_page import LoginPage

class TestRestHandleMute(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver=DriverUtil().get_driver()

        cls.login_page = LoginPage(cls.driver)
        cls.rest_handle=RestHandlePage(cls.driver)
        # 登录
        cls.login_page.login_action()


    @classmethod
    def tearDownClass(cls):
        DriverUtil().quit_driver()


    # 测试小休和工作
    def test_01_rest(self):
        self.rest_handle.rest_work()
    # 测试处理和完成
    def test_02_hanle(self):
        self.rest_handle.hanle_finish()
