import time

from base import init
from base.base_aciton import BaseAciton
from base.assert_action import AssertAction
from base.base_log import Log


#封装小休-工作
class RestHandlePage(BaseAciton):



    def __init__(self,driver):
        BaseAciton.__init__(self,driver)
        self.assert_action=AssertAction(self.driver)
        self.log=Log()

    # 点击小休/工作按钮
    def rest_work(self):
        self.click_element(init.rest_button)
        # 输出日志
        self.log.debug("点击小休")

        # 断言点击小休是否切换 当前状态为    小休   等待
        rest_assert_error_photo = "rest_assert_error_photo"
        self.assert_action.assert_in("小休",self.find_element(init.status_element).text,rest_assert_error_photo)
        self.click_element(init.rest_button)
        # 输出日志
        self.log.debug("点击工作")
        self.assert_action.assert_in("等待", self.find_element(init.status_element).text, rest_assert_error_photo)


    def hanle_finish(self):
        self.click_element(init.handle_button)
        # 输出日志
        self.log.debug("点击处理")
        time.sleep(3)

        # 断言点击处理时是否切换 当前状态为    话前处理   等待
        handle_assert_error_photo = "handle_assert_error_photo"
        self.assert_action.assert_in("话前处理",self.find_element(init.status_element).text,handle_assert_error_photo)
        self.click_element(init.handle_button)
        # 输出日志
        self.log.debug("点击完成")
        self.assert_action.assert_in("等待",self.find_element(init.status_element).text,handle_assert_error_photo)


