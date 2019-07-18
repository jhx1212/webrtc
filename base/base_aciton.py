

class BaseAciton:
    def __init__(self,driver):
        self.driver = driver


    #封装点击操作
    def click_element(self,loc):
        #调用自己定义的find_element方法
        self.find_element(loc).click()

    def input_element_content(self,loc,content):
        self.find_element(loc).send_keys(content)

    """
      loc代表要传递一个定位元素用的元祖进来 返回找到的元素
    """
    def find_element(self, loc):
        #在找元素之前 隐形等待等待
        self.driver.implicitly_wait(10)
        return self.driver.find_element(loc[0], loc[1])

