import time

from base import init
from base.base_aciton import BaseAciton
from base.base_log import Log

# 封装进入主页后拨打电话
class CallOutPage(BaseAciton):

    def __init__(self, driver):
        BaseAciton.__init__(self, driver)
        self.log=Log()

    # 每个功能定义到函数里
    # 输入电话号码
    def input_call_num(self):
        self.click_element(init.logon_page_callnum_element)
        self.input_element_content(init.logon_page_callnum_element,init.logon_page_callnum)

    # 点击拨打电话按钮
    def call_out(self):
        self.click_element(init.logon_page_callout_button)


    # 挂断电话
    def hang_up(self):
        self.click_element(init.logon_page_hang_up_button)


    # 通话中测试静音和结束静音
    def mute_voiced(self):
        self.click_element(init.mute_button)
        time.sleep(5)
        self.click_element(init.mute_button)


#     场景1:外拨电话接通后测试静音功能,座席端挂断(接听)
    def spectacle_01(self):
        self.input_call_num()
        time.sleep(2)
        self.call_out()
        time.sleep(10)
        self.mute_voiced()
        time.sleep(5)
        self.hang_up()
        self.log.debug("外拨电话接听后测试静音功能ok")



 #     场景2:外拨电话10秒后坐席挂机(未接听)
    def spectacle_02(self):
        self.input_call_num()
        self.call_out()
        time.sleep(10)
        self.hang_up()
        self.log.debug("外拨电话10秒后坐席挂机ok")


#       场景3: 外拨电话,等到自然挂断(未接听)
    def spectacle_03(self):
        self.input_call_num()
        self.call_out()
        time.sleep(62)
        self.log.debug("外拨电话客户不接通,等到自然挂断ok")


