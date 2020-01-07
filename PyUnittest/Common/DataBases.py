# -*- coding: utf-8 -*-
"""
接口：连接数据库
创建人：魏奇
更新人：魏奇
更新时间：2019-07-16

pymysql.Connect()参数说明
host(str):      MySQL服务器地址
port(int):      MySQL服务器端口号
user(str):      用户名
passwd(str):    密码
db(str):        数据库名称
charset(str):   连接编码

connection对象支持的方法
cursor()        使用该连接创建并返回游标
commit()        提交当前事务
rollback()      回滚当前事务
close()         关闭连接

cursor对象支持的方法
execute(op)     执行一个数据库的查询命令
fetchone()      取得结果集的下一行
fetchmany(size) 获取结果集的下几行
fetchall()      获取结果集中的所有行
rowcount()      返回数据条数或影响行数
close()         关闭游标对象
"""

import pymysql


class Mysql_links():

    #初始话数据,数据库配置
    def __init__(self,host,username,password,dbname,port=3306):
        self.host = host #数据库地址
        self.port = port #端口
        self.username = username #用户名
        self.password = password #密码
        self.dbname = dbname #库名

    #连接mysql数据库
    def mysqldb(self):
        #打开数据库连接
        self.dbmysql = pymysql.connect(self.host,self.username,self.password,self.dbname) #参数：链接，用户名，密码，库名
        #使用cursor()方法创建一个游标对象cursor
        self.cursor = self.dbmysql.cursor()

    #查询语句
    def querydata(self,sql):
        #sql语句
        self.sql = sql
        # #sql语句
        # self.sql = "select * from uc_order where order_id = %s" #sql语句
        # self.datas = ('15592055440670000') #sql参数

        try:
            #执行语句，并输出结果
            # self.cursor.execute(self.sql % self.datas ) #执行sql语句
            self.cursor.execute(self.sql) #执行sql语句
        except Exception as err: #常规错误的基类
            print("查询失败，原因为：%s" % err)
        else:
            self.datas = self.cursor.fetchall()     #获取结果集中的所有行
            print('查询成功共%s条数据' % self.cursor.rowcount) #self.cursor.rowcount，受影响的数据
            print(self.datas) #打印结果
            return self.datas           #返回数据
        finally:
            #关闭连接
            self.cursor.close()         #关闭游标对象
            self.dbmysql.close()        #关闭数据库连接


    #新增语句
    def adddata(self,sql):
        #sql语句
        self.sql = sql

        try:
            #执行语句，并输出结果
            self.cursor.execute(self.sql) #执行sql语句
        except Exception as err: #常规错误的基类
            print("新增失败，原因为：%s" % err)
        else:
            self.cursor.commit()       #提交数据，仅做插入，修改，删除时调用
            print('新增成功共%s条数据' % self.cursor.rowcount)  #self.cursor.rowcount，受影响的数据
        finally:
            #关闭连接
            self.cursor.close()         #关闭游标对象
            self.dbmysql.close()        #关闭数据库连接

    #修改语句
    def alterdata(self,sql):
        #sql语句
        self.sql = sql

        try:
            #执行语句，并输出结果
            self.cursor.execute(self.sql) #执行sql语句
        except Exception as err: #常规错误的基类
            print("修改失败，原因为：%s" % err)
        else:
            self.cursor.commit()       #提交数据，仅做插入，修改，删除时调用
            print('修改成功共%s条数据' % self.cursor.rowcount)  #self.cursor.rowcount，受影响的数据
        finally:
            #关闭连接
            self.cursor.close()         #关闭游标对象
            self.dbmysql.close()        #关闭数据库连接

    #删除语句
    def deletedata(self,sql):
        #sql语句
        self.sql = sql

        try:
            #执行语句，并输出结果
            self.cursor.execute(self.sql) #执行sql语句
        except Exception as err: #常规错误的基类
            print("删除失败，原因为：%s" % err)
        else:
            self.cursor.commit()       #提交数据，仅做插入，修改，删除时调用
            print('删除成功共%s条数据' % self.cursor.rowcount)  #self.cursor.rowcount，受影响的数据
        finally:
            #关闭连接
            self.cursor.close()         #关闭游标对象
            self.dbmysql.close()        #关闭数据库连接

if __name__ == "__main__":
    # host = "172.31.10.8" #数据库地址
    # username = "chome" #用户名
    # password = "Bd383975f781d1e25d7a94!26" #密码
    # dbname = "chome" #库名
    # db = Mysql_links(host,username,password,dbname)
    # db.mysqldb()
    # A = db.querydata("select * from uc_order where order_id = %s" % ('15592055440670000'))
    # print(A[0][15])

    Mysql_links()