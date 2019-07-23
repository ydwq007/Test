# -*- coding: utf-8 -*-
"""
接口：发送测试报告
创建人：魏奇
更新人：魏奇
更新时间：2019-07-11
"""

import smtplib
import os.path as pth
import time,os
from email.mime.text import MIMEText #发送字符串的邮件
from email.header import Header
from email.mime.multipart import MIMEMultipart #处理多种形态的邮件主体，包括发送附件
from email.mime.image import MIMEImage #处理图片
from email.mime.application import MIMEApplication #处理附件，MIMEApplication默认子类型是application/octet-stream

#发送附件邮件配置
def email_appendix(content,title, from_name, from_address, to_address,serverport, serverip, username, password):
    mg = MIMEMultipart()
    mg["Subject"] = Header(title,"utf-8") #邮件标题
    # to_addrs = to_address.split(',')
    mg["To"] = Header(",".join(to_address),"utf-8") #收件地址,多个邮箱按照逗号拼接为字符串
    mg["From"] = Header(from_name,"utf-8") #发件地址

    mg.attach(MIMEText(content,"html","utf-8"))#邮件正文内容

    # 构造附件，传送当前目录下的 test.txt 文件
    appendix = MIMEText(open(r"..\TestResults\test_result.html", 'rb').read(), 'base64', 'utf-8')
    appendix["Content-Type"] = 'application/octet-stream'
    appendix["Content-Disposition"] = 'attachment; filename="test_result.html"'
    mg.attach(appendix)

    try:
        s = smtplib.SMTP_SSL(serverip, serverport) #发件人邮箱中的SMTP服务器
        s.login(username, password) #发件人邮箱的用户名和密码
        s.sendmail(from_address, to_address, mg.as_string()) #接收邮箱可能有多个，所以是列表存储；参数发件人邮箱账号、收件人邮箱账号、发送邮件
        print("发送邮件成功时间为：%s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #格式化本地时间
    except Exception as err: #常规错误的基类
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("邮件发送失败，原因为：%s" % err)
        # respose.content.decode('utf-8')
    finally:
        s.quit()




#发送字符串邮件配置
def email_string(content, title, from_name, from_address, to_address, serverport, serverip, username, password):
    #邮件内容
    msg = MIMEText(content,"html","utf-8") #创建普通消息对象，参数为：文件内容，格式，编码
    msg["Subject"] = Header(title,"utf-8") #邮件标题
    msg["To"] = Header(to_address,"utf-8") #收件地址to_address为string格式
    msg["From"] = Header(from_name,"utf-8") #发件地址

    try:
        s = smtplib.SMTP_SSL(serverip, serverport) #发件人邮箱中的SMTP服务器
        s.login(username, password) #发件人邮箱的用户名和密码
        s.sendmail(from_address, to_address,msg.as_string()) #接收邮箱可能有多个，所以是列表存储；参数发件人邮箱账号、收件人邮箱账号、发送邮件
        print("发送邮件成功时间为：%s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #格式化本地时间
    except Exception as err: #常规错误的基类
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("邮件发送失败，原因为：%s" % err)
        # respose.content.decode('utf-8')
    finally:
        s.quit()

#获取最新文件
def find_new_file(dir): #参数为文件夹路径
    file_lists = os.listdir(dir) #查找路径下的所有文件
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
    if not os.path.isdir(dir + "\\" + fn)
    else 0)
    file = os.path.join(dir, file_lists[-1])
    return file

#发送邮件
def sendemail(send_content=2,file=2):
    #邮件接收地址
    adresses = ["weiqi@seeyon.com","775636762@qq.com"]

    #服务器参数
    config = {
        "from": "775636762@qq.com", #服务器邮箱地址
        "from_name": "Python接口自动化测试框架:", #邮件主题
        "to": adresses, #邮件接收地址
        "serverip": "smtp.qq.com", #邮件服务器
        "serverport": "465", #邮件服务器端口
        "username": "775636762@qq.com", #服务器邮箱用户名
        "password": "txhattvlgxzxbfdc"  # 服务器邮箱密码，使用QQ邮箱的SMTP授权码
    }
    #邮件标题
    title = "Python接口自动化测试报告  %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if file == 1:#1表示固定文件，其他表示最新文件
        #发送固定文件
        with open(r"..\TestResults\test_result.html", "rb") as file:#读取二进制
            mail_body = file.read()
    else:
        #发送最新文件
        # dir = r"..\TestResults"  # 指定文件目录
        dir = "../TestResults"  # 指定文件目录
        new_file = find_new_file(dir)  # 查找最新的html文件
        with open(r'%s'% new_file, "rb") as file:
            mail_body = file.read()

    if send_content == 1: #1表示字符串邮件，其他表示附件邮件
        #调用字符串邮箱配置
        email_string(mail_body,title,config["from_name"],config["from"],config["to"],config["serverport"],config["serverip"],
                 config["username"],config["password"])
    else:
        #调用附件邮箱配置
        email_appendix(mail_body,title,config["from_name"],config["from"],config["to"],config["serverport"],config["serverip"],
                       config["username"], config["password"])

if __name__ == "__main__":
    sendemail() #第一个参数（1表示字符串邮件，2表示发送附件邮件，默认2），第二个参数（#1表示固定文件，2表示最新文件，默认2）