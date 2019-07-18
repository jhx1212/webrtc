import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import alert_is_present

from base import init
from base.base_aciton import BaseAciton
from base.base_log import Log

# 封装进入主页后拨打电话
class RingSoundPage(BaseAciton):

    def __init__(self, driver):
        BaseAciton.__init__(self, driver)
        self.alert_is_present=alert_is_present()
        self.log=Log()


    #     封装回环声音测试15秒
    def ring_sound(self):
        self.click_element(init.ring_sound_button)
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.log.debug("测试回环音")


        # 判断弹框是否出现，如果出现则点击取消，否则无须处理
        result = self.alert_is_present.__call__(self.driver)
        if result:
            result.accept()
        else:
            pass

