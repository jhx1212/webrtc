
from selenium.webdriver.common.by import By
import os
from tools.readconfig import ReadConfig


"""
读取配置文件
"""
# project_path=E:\automaticScript\webrtc0710
config_file_path=os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))

prj_path = read_config.getValue('projectConfig','project_path')


"""测试套件执行的代码文件   win10"""
discover_path = os.path.join(prj_path,"script")

"""
# 日志路径
"""
log_path = os.path.join(prj_path,'logs')


"""
截图文件路径
"""
img_path = os.path.join(prj_path,'photo')

"""
测试报告路径
"""
report_path = os.path.join(prj_path,'report')



"""
# 邮件收件人
"""
# rec_address = ('895942976@qq.com','jiahx@infobird.com')
# send_mail_type = "QQ_mail"
# sender_name = "895942976@qq.com"
# sender_pswd = "bullbzwziwxrbdfj"
# mail_host = "smtp.qq.com"
# mail_port = 465
send_mail_type = "163_mail"
sender_name = "18801331197@163.com"
sender_pswd = "18801331197aaa"
mail_host = "smtp.163.com"
mail_port = 0
# send_mail_type = "infobird_mail"

rec_address = 'jiahx@infobird.com'

"""
qq邮箱授权码895942976@qq.com
163邮箱授权码18801331197@163.com
"""
# 发件人邮箱及授权码
qq_mail="895942976@qq.com"
qq_mail_no = "ibryecqjkpprbeba"
phono_no = "18801331197"
phono_mail_no = "jhx506922"


"""
[browerType]浏览器类型
"""
# browserName = "Firefox"
browserName = "Chrome"
# browserName = "IE"


"""
1.登录页面
"""
url="https://webrtctest.infobird.com/"

login_logo = (By.ID, "btnLogo")
login_username = (By.ID, "editAccount")
login_password = (By.ID, "editPassword")
login_button = (By.ID, "btnLogin")


# 账号和密码
login_page_username="tiaocuo2@zj.com"
login_page_password="tiaocuo2@zj.com"


# 登录后断言是都登录成功
# 显示当前登录账号
login_page_username_element=(By.ID,"lblAgentRole")
# 用户名或密码错误时,显示状态为未登录
login_page_error_element=(By.ID,"lblAgentState")



"""

2主页面,logonpage"
"""
# 电话号码输入框
logon_page_callnum_element=(By.ID,"editPhoneNum")
# 测试用的电话号码
logon_page_callnum="18801331197"
# logon_page_callnum="53709159"
# 拨打按钮
logon_page_callout_button=(By.ID,"imgDial")
# 挂断按钮
logon_page_hang_up_button=(By.ID,"imgProcess")
# 登录按钮
logon_page_logout_button=(By.ID,"btnLogout")



"""
3主页面的小休 -- 工作
         处理 --  完成
         静音 --  结束静音
"""
rest_button=(By.ID,"imgPark")

handle_button=(By.ID,"imgProcess")

mute_button=(By.ID,"imgMute")


"""
回环声音测试

"""
ring_sound_button=(By.ID,"autoTest")



"""
状态显示---断言用
"""
status_element=(By.ID,"lblAgentState")
text_wait="等待"
text_rest="小休"
text_handle="话前处理"
text_dial="拨号"
text_call="通话"