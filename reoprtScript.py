
from tools import sendmail
import unittest
import time
import os
from base import init
from tools.HTMLTestRunner import HTMLTestRunner


progectPath = init.prj_path
# 定义测试套件
# discover = unittest.defaultTestLoader.discover("./script/")
# discover = unittest.defaultTestLoader.discover(progectPath+"\script")
discover = unittest.defaultTestLoader.discover(init.discover_path)
# print(progectPath+"\script")

# 指定生成报告目录及文件名称
# report_name = "./report/{}.html".format(time.strftime("%Y_%m_%d_%H_%M_%S"))
report_name = "%s/%s.html" % (init.report_path,time.strftime("%Y_%m_%d_%H_%M_%S"))

# report_name = init.report_path.join("%s.html" % time.strftime("%Y_%m_%d_%H_%M_%S"))
print(report_name)

# HtmlTestRunner运行并生成报告
with open(report_name,"wb") as f:
    HTMLTestRunner(stream=f,title="WebRTC测试报告",description="win 10").run(discover)

# 将测试报告发送邮件
sender_mail=sendmail.SendMail()
sender_mail.send_mail()


