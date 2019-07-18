import time
import unittest



from base.base_driver import DriverUtil
from page.call_out_page import CallOutPage
from page.login_page import LoginPage


class TestCallOut(unittest.TestCase):

    time_s = time.strftime("%Y_%m_%d-%H_%M_%S")

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil().get_driver()
        cls.login_page = LoginPage(cls.driver)
        cls.call_out_page=CallOutPage(cls.driver)
        # 登录操作
        cls.login_page.login_action()


    @classmethod
    def tearDownClass(cls):
        DriverUtil().quit_driver()


    #     场景1:外拨电话接通后测试静音功能,座席端挂断(接听)
    def test_01_call_out_action(self):
        time.sleep(2)
        self.call_out_page.spectacle_01()
        time.sleep(5)
    #     场景2:外拨电话10秒后坐席挂机(未接听)
    def test_02_call_out__action(self):
        time.sleep(2)
        self.call_out_page.spectacle_02()
#       场景3: 外拨电话,等到自然挂断(未接听)
    time.sleep(5)
    def test_03_call_out__action(self):
        time.sleep(2)
        self.call_out_page.spectacle_03()
