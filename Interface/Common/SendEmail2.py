# -*- coding: utf-8 -*-
#发送邮件

import smtplib
import os.path as pth
import time,os
from email.mime.text import MIMEText #发送字符串的邮件
from email.header import Header
from email.mime.multipart import MIMEMultipart #处理多种形态的邮件主体，包括发送附件
from email.mime.image import MIMEImage #处理图片
from email.mime.application import MIMEApplication #处理附件，MIMEApplication默认子类型是application/octet-stream


class SendEmails:
    #初始化数据
    def __init__(self,title,from_name,from_address,to_address,serverport,serverip,username,password,content=""):
        self.content = content
        self.title = title
        self.from_name = from_name
        self.from_address = from_address
        self.to_address = to_address
        self.serverport = serverport
        self.serverip = serverip
        self.username = username
        self.password = password

    #获取最新文件
    def find_new_file(self,dir): #参数为文件夹路径
        file_lists = os.listdir(dir) #查找路径下的所有文件
        file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
        if not os.path.isdir(dir + "\\" + fn)
        else 0)
        file = os.path.join(dir, file_lists[-1])
        return file

    #发送字符串邮件配置
    def email_string(self):
        # #发送固定文件
        # with open(r"D:\IdeaProjects\seeyon\Interface\TestResults\test_result.html", "rb") as file:#读取二进制
        #     mail_body = file.read()

        #发送最新文件
        dir = r"D:\IdeaProjects\seeyon\Interface\TestResults"  # 指定文件目录
        mail_body = self.find_new_file(dir)  # 查找最新的html文件

        #邮件内容
        msg = MIMEText(mail_body,"html","utf-8") #创建普通消息对象，参数为：文件内容，格式，编码
        msg["Subject"] = Header(self.title,"utf-8") #邮件标题
        msg["To"] = Header(self.to_address,"utf-8") #收件地址to_address为string格式
        msg["From"] = Header(self.from_name,"utf-8") #发件地址

    #发送附件邮件配置
    def email_appendix(self):
        mg = MIMEMultipart()
        # 构造附件，传送当前目录下的 test.txt 文件
        appendix = MIMEText(open(r"D:\IdeaProjects\seeyon\Interface\TestResults\test_result.html", 'rb').read(), 'base64', 'utf-8')
        appendix["Content-Type"] = 'application/octet-stream'
        appendix["Content-Disposition"] = 'attachment; filename="test_result.html"'
        mg.attach(appendix)
        return mg

    #发送邮件
    def sendemails(slef):
        try:
            s = smtplib.SMTP_SSL(slef.serverip,slef.serverport) #发件人邮箱中的SMTP服务器
            s.login(slef.username,slef.password) #发件人邮箱的用户名和密码
            s.sendmail(slef.from_address,slef.to_address,slef.mg.as_string()) #接收邮箱可能有多个，所以是列表存储；参数发件人邮箱账号、收件人邮箱账号、发送邮件
            print("发送邮件成功时间为：%s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #格式化本地时间
        except Exception as err: #常规错误的基类
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("邮件发送失败，原因为：%s" % err)
            # respose.content.decode('utf-8')
        finally:
            s.quit()

        send_content = 2 #1表示字符串邮件，其他表示附件邮件
        if send_content == 1:
            #调用字符串邮箱配置
            slef.email_string()
        else:
            #调用附件邮箱配置
            slef.email_appendix()


if __name__ == "__main__":
    #邮件接收地址
    adresses = ["weiqi@seeyon.com"]

    #服务器参数
    config = {
        "from": "775636762@qq.com", #服务器邮箱地址
        "from_name": "Python接口自动化测试框架:", #邮件主题
        "to": adresses[0], #邮件接收地址
        "serverip": "smtp.qq.com", #邮件服务器
        "serverport": "465", #邮件服务器端口
        "username": "775636762@qq.com", #服务器邮箱用户名
        "password": "txhattvlgxzxbfdc"  # 服务器邮箱密码，使用QQ邮箱的SMTP授权码
    }
    #邮件标题
    title = "Python接口自动化测试报告"
    send = SendEmails(title, config["from_name"], config["from"], config["to"], config["serverport"], config["serverip"],config["username"], config["password"])
    send.sendemails()