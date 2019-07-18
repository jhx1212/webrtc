
import os,time
import smtplib
from email.mime.text import MIMEText
from base import init
from base.base_log import Log

#测试报告路径
# init文件中全局参数里report_path报告路径存放位置(截止到report文件夹)
reportPath = init.report_path

# 配置收发件人
recAddress = init.rec_address

# QQ邮箱,发件人的用户名和密码,授权码,服务器,端口
sender_name = init.sender_name
sender_pswd = init.sender_pswd
mail_host = init.mail_host
mail_port = init.mail_port
# 发件人使用讯鸟公司邮箱的用户名和密码
# mail_host = 'smtp.exmail.qq.com'
# sender_name = '***@infobird.com'
# sender_pswd = '***'

logger = Log()
class SendMail():
    '''定义发送邮件'''
    def __init__(self, receiver=None):
        # self.logger=Log()
        """接收邮件的人：list or tuple"""
        if receiver is None:
            self.sendTo = recAddress
        else:
            self.sendTo = receiver

    def __get_report(self):
        '''获得最新测试报告'''
        #获取目录下的所有文件
        lists = os.listdir(reportPath)
        # print(lists)
        # 排序之后取到最新的报告
        lists.sort()
        new_report_name = lists[-2]
        # print(new_report_name)
        print('The new report name: {0}'.format(new_report_name))
        return new_report_name

    def __messages(self):
        '''生成邮件内容'''
        # 定义正文,最新的报告为文件正文,引用__get_report方法得到
        new_report = self.__get_report()
        # print("new_report:%s" % new_report)
        path_s=os.path.join(reportPath,new_report)
        # 打开最新的报告
        f = open(path_s, "rb")
        mail_body = f.read()
        f.close()

        self.msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        # 定义标题
        self.msg['Subject'] = "webrtc测试报告"
        # 定义发送人和接收人
        self.msg['From'] = sender_name
        self.msg['To'] = recAddress

    def send_mail(self):
        """发送邮件"""
        self.__messages()
        # 发件箱是qq邮箱
        if init.send_mail_type == "QQ_mail":
            try:
                smtp = smtplib.SMTP_SSL(mail_host,mail_port)
                smtp.login(sender_name,sender_pswd)
                smtp.sendmail(sender_name, recAddress, self.msg.as_string())
                smtp.quit()
                logger.info("邮件发送成功")
            except Exception:
                logger.error("邮件发送失败")
                raise
        elif init.send_mail_type == "163_mail":
            try:
                smtp=smtplib.SMTP()
                smtp.connect(mail_host,mail_port)
                smtp.login(sender_name,sender_pswd)
                smtp.sendmail(sender_name,recAddress,self.msg.as_string())
                smtp.quit()
                logger.info("邮件发送成功")
            except Exception:
                logger.error("邮件发送失败")
                raise





if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send_mail()






