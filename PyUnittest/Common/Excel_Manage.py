# -*- coding: utf-8 -*-
"""
接口：Excle读取和写入
创建人：魏奇
更新人：魏奇
更新时间：2020-01-18 10:23
描述：
"""

import xlrd,xlwt,openpyxl
from xlutils.copy import copy

# xlrd和xlwt处理的是xls文件，单个sheet最大行数是65535
class excelprocess_xl():

    # 读取工作簿中的数据
    def read_excel_xls(self,path,sheet_name=""):

        workbook = xlrd.open_workbook(path)  # 打开工作簿

        #指定表名打印数据
        if len(sheet_name) == 0:
            sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
            sheetname = sheets[0]
            worksheet = workbook.sheet_by_name(sheetname)  # 获取工作簿中所有表格中的的第一个表格
        else:
            sheetname = sheet_name
            worksheet = workbook.sheet_by_name(sheetname)  # 按照表名获取工作簿中所有表格中的的表格

        rows = worksheet.nrows # 统计行数
        cols = worksheet.ncols # 统计列数
        # print("\n内容读取成功。文件名为:%s，表名为:%s，共%s行%s列数据" % (path,sheetname,rows,cols))

        for i in range(0, rows):
            # print("第%s行数据" % (i+1))
            for j in range(0, cols):
                worksheet.cell_value(i,j)
                # print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据
            print()

    def write_excel_xls(self,path,value,sheet_name):
        index = len(value)  # 获取需要写入数据的行数
        index1 = len(value[0]) # 获取需要写入数据的列数

        workbook = xlwt.Workbook()  # 新建一个工作簿
        sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格

        for i in range(0, index):
            for j in range(0, len(value[i])):
                sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
        workbook.save(path)  # 保存工作簿

        # print("\n内容写入成功。文件名为:%s，表名为:%s，共%s行%s列数据" % (path,sheet_name,index,index1))
        excelprocess_xl.read_excel_xls("",path,sheet_name)


    def write_excel_xls_append(self,path,value,sheet_name=""):

        index = len(value)  # 获取需要写入数据的行数
        index1 = len(value[0]) # 获取需要写入数据的列数

        workbook = xlrd.open_workbook(path)  # 打开工作簿
        if len(sheet_name) == 0:
            sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
            sheetname = sheets[0]
            worksheet = workbook.sheet_by_name(sheetname)  # 获取工作簿中所有表格中的的第一个表格
        else:
            sheetname = sheet_name
            worksheet = workbook.sheet_by_name(sheetname)  # 按照表名获取工作簿中所有表格中的的表格

        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格

        for i in range(0, index):
            for j in range(0, len(value[i])):
                new_worksheet.write(i+rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
        new_workbook.save(path)  # 保存工作簿

        # print("\n内容追加成功。文件名为:%s，表名为:%s，共%s行%s列数据" % (path,sheetname,index,index1))
        excelprocess_xl.read_excel_xls("",path,sheet_name)

    def write_excel_xls_modify(self,path,row,col,value,sheet_name="",style=1,original_row=1,original_col=1):


        workbook = xlrd.open_workbook(path)  # 打开工作簿
        if len(sheet_name) == 0:
            sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
            sheetname = sheets[0]
            worksheet = workbook.sheet_by_name(sheetname)  # 获取工作簿中所有表格中的的第一个表格
        else:
            sheetname = sheet_name
            worksheet = workbook.sheet_by_name(sheetname)  # 按照表名获取工作簿中所有表格中的的表格

        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        # new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
        new_worksheet = new_workbook.get_sheet(sheetname)  # 获取转化后工作簿中的指定表格
        rows = worksheet.nrows # 统计行数
        cols = worksheet.ncols # 统计列数

        if style == 1:
            new_worksheet.write(row-1,col-1,value)  # 修改指定格子的数据
        elif style == 2:
            for i in  range(original_col-1,col):
                new_worksheet.write(row-1,i,value)  # 修改指定行的指定列到指定列的数据，默认从1列开始
        elif style == 3:
            for j in range(original_row-1,row):
                new_worksheet.write(j,col-1,value)  # 修改指定列的指定行到指定行的数据，默认从1行开始
        else:
            for i in range(original_row-1,row):
                for j in range(original_col-1,col):
                    new_worksheet.write(i,j,value)  # 修改(1,1)到（row,col）区域内的数据，默认从1行1列开始
        new_workbook.save(path)  # 保存工作簿

        # print("\n内容修改成功。文件名为:%s，表名为:%s，修改位置为：%s行%s列" % (path,sheetname,row,col))
        excelprocess_xl.read_excel_xls("",path,sheet_name)


# 使用openpyxl函数，最大行数达到1048576
class excelprocess_op():

    def __init__(self,read_file="",read_sheet="",write_file="",write_sheet=""):
        self.read_file = read_file
        self.write_file = write_file
        self.read_sheet = read_sheet
        self.write_sheet = write_sheet

    def readExel(self):
        filename = self.read_file
        readsheet = self.read_sheet
        inwb = openpyxl.load_workbook(filename)  # 读文件
        # print("\n读取文件名称：%s\n" % filename)

        sheetnames = inwb.get_sheet_names()  # 获取读文件中所有的sheet，通过名字的方式
        # print("\n读取表名称：%s\n" % readsheet)

        ws = inwb.get_sheet_by_name(readsheet)  # 获取指定sheet内容
        rows = ws.max_row  # 获取sheet的最大行数
        cols = ws.max_column  # 获取sheet的最大列数
        for r in range(1,rows+1):
            for c in range(1,cols+1):
                square_value = ws.cell(r,c).value
                # print("\nsheet表第%s行第%s列内容：\n%s"  % (r,c,square_value))# 打印每一行每一列的值
            # if r==10:
            #     break
        # print("\n文件%s的表%s，共%s行%s列数据\n" % (filename,readsheet,rows,cols))

    def writeExcel(self,row,col,value,type = 1):

        filename = self.write_file
        comment = value

        outwb = openpyxl.Workbook()  # 打开一个将写的文件
        outws = outwb.create_sheet(index=0)  # 在将写的文件创建sheet

        # 填充从0开始到指定的行和列区域，相同值
        if type == 1:
            for i in range(1,row+1): # 行数
                for j in range(1,col+1): # 列数
                    outws.cell(i, j).value = comment  # 写文件
                print(i)
        elif type == 2: # 填充指定的列，相同值
            for i in range(1,row+1): # 行数
                outws.cell(i, col).value = comment  # 写文件
                print(i)
        elif type == 3: # 填充指定的行，相同值
            for j in range(1,col+1): # 列数
                outws.cell(row, j).value = comment  # 写文件
                print(j)
        elif type == 4:  # 填充指定某一个格
            outws.cell(row, col).value = comment  # 写文件
        else:
            # 添加一行到当前sheet的最底部（即逐行追加从第一行开始） iterable必须是list,tuple,dict,range,generator类型的。
            # 1,如果是list,将list从头到尾顺序添加。
            # 2，如果是dict,按照相应的键添加相应的键值。
            for i in range(1,row+1):
                outws.append(comment)

        saveExcel = filename
        outwb.save(saveExcel)  # 一定要记得保存

if __name__ == "__main__":

    value1 = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6M" \
            "TU3OTI1MDM4OCwic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzkyOTM1ODgsInVpZCI6I" \
            "jE1NjM0NDI1NDcwMTkwMDAwIn0.Qq29GgNJPbCCn8I5zWVPjH3a4m7qqf2OMuX6BPxgZc0"
    value2 = ["A","B","C","D","E","F"]
    file_path = r"D:\IdeaProjects\data\test.xlsx"
    row = 100
    col = 5
    style = 5

    book_name_xls = 'xls格式测试工作簿.xls'
    book_name_xls1 = r'D:\IdeaProjects\interfacetest\Experiment\Python_Excel\xls格式测试工作簿.xls'
    sheet_name_xls = 'xls格式测试表 (2)'
    value_title = [["姓名", "性别", "年龄", "城市", "职业"]]
    value3 = [["张三", "男", "19", "杭州", "研发工程师"],
              ["李四", "男", "22", "北京", "医生"],
              ["王五", "女", "33", "珠海", "出租车司机"],]
    value4 = [["Tom", "男", "21", "西安", "测试工程师"],
              ["Jones", "女", "34", "上海", "产品经理"],
              ["Cat", "女", "56", "上海", "教师"],]
    style1 =1
    mdvalue = """{
        "Content-Type": "application/json",
        "Authorization":"Bearer %s"
    } """

    # excle_op = excelprocess_op(write_file=file_path,read_file=file_path,read_sheet="Sheet1")
    # excle_op.writeExcel(row,col,value1,type=style)
    # excle_op.readExel()

    excel_xl = excelprocess_xl()
    # excel_xl.write_excel_xls(book_name_xls,value_title, sheet_name_xls)
    # excel_xl.write_excel_xls_append(book_name_xls, value3)
    # excel_xl.write_excel_xls_append(book_name_xls,value4,sheet_name_xls)
    excel_xl.write_excel_xls_modify(book_name_xls1,6,4,mdvalue,sheet_name=sheet_name_xls,style=style1)
