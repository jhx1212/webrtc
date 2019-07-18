
import logging,os,sys,time
import logging.handlers
from base import init


log_path = init.log_path

class Log:
    def __init__(self):
        # self.logname = os.path.join(log_path,'{0}.logs'.format(time.strftime("%Y-%m-%d")))
        self.log_dir = os.getcwd().split("script")[0] + "\logs"
        self.log_dir = init.log_path
        # self.log_dir =sys.argv[0]
        # print(os.getcwd())
        # print(os.getcwd().split("script")[0])
        # print(os.getcwd().split("script")[-1])
        # print(self.log_dir)
        # 日志的名称
        time_s = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
        self.log_name = (self.log_dir + "\logs%s.logs" % time_s)
        # print(self.log_name)

    def print_console(self,level,message):

        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        #创建一个handler ,用于写入日志文件
        fh = logging.FileHandler(self.log_name,'a',encoding='utf-8')


        # 创建一个handler ,用于写入日志文件,每一分钟写一次,保留10个日志文件
        # fh=logging.handlers.TimedRotatingFileHandler(self.log_name, when="M", interval=2, backupCount=10,encoding='utf-8')


        # 设置日志级别为debug
        fh.setLevel(logging.DEBUG)


        #创建一个handler，用于输出到控制台
        sh = logging.StreamHandler()
        # 设置日志级别为debug
        sh.setLevel(logging.DEBUG)


        #定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)


        #给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(sh)

        #记录一条记录

        if level == 'debug':
            logger.debug(message)
        elif level == 'info':
            logger.info(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)


        # 移除事件与事件处理程序之间的关联
        logger.removeHandler(sh)
        logger.removeHandler(fh)

        #关闭打开的文件
        fh.close()


    # 封装不同级别的日志
    def info(self,message):
        self.print_console('info',message)

    def debug(self,message):
        self.print_console('debug',message)

    def warning(self,message):
        self.print_console('warning',message)

    def error(self,message):
        self.print_console('error',message)


if __name__ == '__main__':
    sendMail = Log()
    sendMail.info("555")