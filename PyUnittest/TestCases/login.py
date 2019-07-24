# -*- coding: utf-8 -*-
"""
接口：登录的自动化脚本 - selenium
创建人：魏奇
更新人：魏奇
更新时间：2019-07-15
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By #支持定位的分类
# import logging
# logging.basicConfig(level=logging.DEBUG)
from selenium.webdriver.support import expected_conditions as ec #导入显示预期条件判断方法，并且重名为ec
from selenium.common.exceptions import NoSuchElementException #导入隐式等待
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
from selenium.common.exceptions import TimeoutException

#设置浏览器
#火狐浏览器
# browser = webdriver.Firefox(log_path=r"..\TestResults\geckodriver.log")
#谷歌浏览器
# chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
chrome = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome)

#设置请求网址
# browser.get("https://testchome.seeyon.com")
browser.get("https://testcloud.seeyon.com")

time.sleep(1) #等待1s

print("-------登录前打印信息---------")
#获取当前页面的标题和URL并打印
title = browser.title #当前页面的标题
now_url = browser.current_url #获取当前页面的URL
print(title)
print(now_url)

#定位元素进行登录
browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/span[2]/a[1]').click()#点击登录按键 谷歌和火狐的xpath的值不一样
# browser.find_elements_by_css_selector("#.user-info__login > a:nth-child(1)").click()
browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]").click() #点击用户登录
browser.find_element_by_id("login_common_li").click() #选择账号密码登录
browser.find_element_by_id("login_username").send_keys("gold001") #输入用户名
browser.find_element_by_id("login_password").send_keys("123456") #输入密码
browser.find_element_by_id("login_submit").click() #点击登录按键


#检查元素
browser.set_page_load_timeout(10) #页面载入最长时间
print("-----------检查元素（显示等待）---------")
for i in range(10):
    try:
        el1 = browser.find_element(By.CLASS_NAME,"icon-cart")
        #el = driver.find_element_by_id("useraddr")
        if el1.is_displayed():#如果元素展示
            print(el1)
            print("元素存在，pass")
            time.sleep(1)
            break
        else:
            print("元素不存在，fail")
    except Exception as err:
        print("出现异常，具体如下\n%s" % err)
    finally:
        print(time.ctime())
try:
    WebDriverWait(browser, 5).until(
        ec.presence_of_element_located((By.CLASS_NAME,"icon-cart"))
    )
except TimeoutException as msg: #超时未找到
    print(msg)
finally:
    print(time.ctime())
    print(browser.page_source) #打印页面资源


print("-----------检查元素（隐形等待）-----------")
browser.implicitly_wait(10) #隐形等待时间为10s
try:
    print(time.ctime())
    ys2 = browser.find_element(By.CLASS_NAME,"icon-cart")
    print(ys2)
except NoSuchElementException as msg:
    print(msg)
finally:
    print(time.ctime())

time.sleep(3) #等待3s1
browser.quit() #退出浏览器