
from selenium import webdriver
from base import init
# 定义浏览器对象

class DriverUtil:
    driver = None
    _auto_quit = True



    # 获取驱动
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # cls._driver = webdriver.Firefox()


            # cls._driver = webdriver.Chrome()
            # cls.options = webdriver.ChromeOptions()
            # cls.prefs = {
            #     'profile.default_content_setting_values':
            #         {
            #             'notifications': 2
            #         }
            # }
            # cls.options.add_experimental_option("prefs",cls.prefs)

            # cls.options = webdriver.ChromeOptions()
            # cls.options.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
            if init.browserName == "Firefox":
                cls.driver = webdriver.Firefox()
            elif init.browserName == "Chrome":
                # cls.driver = webdriver.Chrome()
                # 不打开浏览器页面做自动化测试
                cls.opeion = webdriver.ChromeOptions()
                cls.opeion.add_argument("headless")
                cls.driver=webdriver.Chrome(chrome_options=cls.opeion)

            elif init.browserName == "IE":
                cls.driver = webdriver.Ie()

            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
            cls.driver.get(init.url)
        return cls.driver

    # 退出驱动
    @classmethod
    def quit_driver(cls):
        if cls._auto_quit:
            if cls.driver:
                cls.driver.quit()
                cls.driver = None

        # 设置是否自动退出驱动

    @classmethod
    def set_auto_quit(cls, auto_quit):
        cls._auto_quit = auto_quit