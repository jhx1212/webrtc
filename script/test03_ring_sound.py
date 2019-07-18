import unittest



from base.base_driver import DriverUtil
from page.login_page import LoginPage
from page.ring_sound_page import RingSoundPage


class TestCallOut(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil().get_driver()
        cls.ring_sound_page=RingSoundPage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        # 登录
        cls.login_page.login_action()

    @classmethod
    def tearDownClass(cls):
        DriverUtil().quit_driver()


    # 封装未登录状态的回环声音测试
    def test_01_ring_sound(self):
        self.ring_sound_page.ring_sound()