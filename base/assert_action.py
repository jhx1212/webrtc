import time
import unittest

from base.base_driver import DriverUtil

# 封装断言方法
class AssertAction():
    #
    def __init__(self,driver):
        # self.driver=DriverUtil().get_driver()
        self.driver=driver


    def assert_in(self,msg1,msg2,photo_name):
        time_s = time.strftime("%Y_%m_%d-%H_%M_%S")
        try:
            assert msg1==msg2
            # print(msg1)
            # print(msg2)
        except AssertionError:
            self.driver.get_screenshot_as_file("../photo/%s%s.png" % (photo_name,time_s))
            raise