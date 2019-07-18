
import configparser


class ReadConfig:
    """
    专门读取配置文件的，.ini文件格式
    """
    def __init__(self, filename):
        self.configpath = filename
        # 创建类对象
        self.cf = configparser.ConfigParser()
        self.cf.read(self.configpath,encoding="utf-8")

    # 获取配置文件信息
    def getValue(self, env, name):

        # 获取配置文件信息
        return self.cf.get(env,name)

