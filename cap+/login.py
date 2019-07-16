from selenium import webdriver
import time,unittest
from selenium.webdriver.common.by import By #支持定位的分类
import logging
logging.basicConfig(level=logging.DEBUG)
from selenium.webdriver.support import expected_conditions as ec #导入显示预期条件判断方法，并且重名为ec
from selenium.common.exceptions import NoSuchElementException #导入隐式等待
class Login_cases(unittest.TestCase): # 继承unittest.TestCase
    browser = webdriver.Firefox()
    browser.get("https://testcloud.seeyon.com")

    time.sleep(1) #等待1s

    print("-------登录前打印信息---------")
    #获取当前页面的标题和URL并打印
    title = browser.title #当前页面的标题
    now_url = browser.current_url #获取当前页面的URL
    print(title)
    print(now_url)

    #按照id定位元素
    # browser.find_element_by_id("qquin").clear() #清除内容
    # browser.find_element_by_class_name("kw").send_keys("07") #输入
    # browser.find_element_by_class_name("icon-search").click() #点击搜索

    #进行登录
    browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/span[2]/a[1]').click()#点击登录按键
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]").click() #点击用户登录
    browser.find_element_by_id("login_common_li").click() #选择账号密码登录
    browser.find_element_by_id("login_username").send_keys("gold001") #输入用户名
    browser.find_element_by_id("login_password").send_keys("123456") #输入密码
    browser.find_element_by_id("login_submit").click() #点击登录按键

    #检查元素
    print("-----------检查元素（显示等待）---------")
    #print(time.ctime()) #打印时间，转化为字符串
    for i in range(10):
        try:
            el1 = browser.find_element(By.CLASS_NAME,"petname")
            #el = driver.find_element_by_id("useraddr")
            if el1.is_displayed():#如果元素展示
                print("元素存在，pass")
                time.sleep(1)
                break
            else:
                print("元素不存在，fail")
        except:
            print("异常")

    # print("-----------检查元素（隐形等待）-----------")
    # browser.implicitly_wait(10) #隐形等待时间为10s
    # try:
    #     print(time.ctime())
    #     ys2 = browser.find_element(By.ID,"subject").send_keys("123456")
    #     print(ys2)
    # except NoSuchElementException as no:
    #     print(no)

    time.sleep(3) #等待1s
    browser.quit() #退出浏览器

if __name__ == '__main__':
    unittest.main()