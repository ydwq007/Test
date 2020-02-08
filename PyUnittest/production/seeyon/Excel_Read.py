# -*- coding: utf-8 -*-
"""
接口：获取excel里的数据
创建人：魏奇
更新人：魏奇
更新时间：2019-11-20 17:17
描述：
"""

import xlrd,xlwt #python操作excel主要用到xlrd和xlwt这两个库，即xlrd是读excel，xlwt是写excel的库
workbook = None

def open_excel(path):
    """
    打开excel
    :param path: 打开excel文件的位置
    """
    global workbook
    if (workbook == None):
        workbook = xlrd.open_workbook(path, on_demand=True) #路径中不能包含中文，打开文件

def get_sheet(sheetName):
    """
    获取页名
    :param sheetName: 页名
    :return: workbook
    """
    global workbook
    return workbook.sheet_by_name(sheetName) #读取sheet表

def get_rows(sheet):
    """
    获取行号
    :param sheet: sheet
    :return: 行数
    """
    return sheet.nrows

def get_content(sheet, row, col):
    """
    获取表格中内容
    :param sheet: sheet
    :param row: 行
    :param col: 列
    :return:
    """
    return sheet.cell(row, col).value

def release(path):
    """释放excel减少内存"""
    global workbook
    workbook.release_resources()
    del workbook
    # todo:没有验证是否可用