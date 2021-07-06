#  -*- coding: utf-8 -*-
"""
接口：通过读取excel的数据，执行用例
创建人：魏奇
创建时间：2020-04-08 15:57
描述：通过读取excel的数据，执行用例
"""
import xlrd, requests, json, logging
import sys
sys.path.append("./Common")  # 跨目录调用需要配置路径
import Json_data, Excel_Manage
sys.path.append("../TestDatas")
import config, Business_Package
import urllib3


# 打开用例文件
def open_xlsx(filepath):
    """
    :param filepath:
    :return:
    """
    file = xlrd.open_workbook(filepath)
    return file


# 读取用文件，将结果参数化
def read_xlsx(sheet, host, caseno):
    """
    :param sheet:
    :param host:
    :param caseno:
    :return:
    """
    case_no = sheet.col_values(0)  # 返回用例编号列的所有值为列表
    #  print(case_no)
    #  获取用例编号所在的行
    try:
        row = case_no.index(caseno)
        # print(row)  # 打印用例编号
    except Exception as errs:
        print("用例编号%s未找到" % caseno)
        logging.exception("出现问题")
        raise errs

    content = {}  # 初始化字典
    content["Test_Number"] = sheet.cell_value(row, 0)  # 用例编号
    content["Test_Name"] = sheet.cell_value(row, 1)  # 场景名称
    content["Test_Url"] = host + sheet.cell_value(row, 2)  # 接口URL

    is_update_header = sheet.cell_value(row, 3)  # 是否更新信息头（是, 否）
    if is_update_header:
        content["Test_Update"] = is_update_header
    else:
        content["Test_Update"] = "否"

    pre_parameter = sheet.cell_value(row, 4)  # 前置参数
    if pre_parameter:
        content["pre_parameter"] = pre_parameter
    else:
        content["pre_parameter"] = "{}"

    accountpassword = sheet.cell_value(row, 5)  # 账号密码
    if accountpassword:
        content["Test_AccountPassword"] = eval(accountpassword)
    else:
        content["Test_AccountPassword"] = "{}"
    content["Test_Method"] = sheet.cell_value(row, 6)  # 接口请求方法

    headers = sheet.cell_value(row, 7)  # 获取信息头
    if headers:
        content["Test_Headers"] = json.loads(headers)  # 接口请求头, 转为为字典
    else:
        content["Test_Headers"] = config.headers

    content["Test_Data"] = json.loads(sheet.cell_value(row, 8))  # 接口入参, 转为为字典
    content["Test_Except"] = sheet.cell_value(row, 9)  # 关键字匹配预期值

    MatchType = sheet.cell_value(row, 10)  # 匹配方式
    if MatchType:
        content["Match_Type"] = MatchType
    else:
        content["Match_Type"] = 1
    content["Path_Except"] = sheet.cell_value(row, 11)  # 路径匹配预期值

    return content

#  更新信息头
# def update_header(file_path, sheet_name, host, caseno, system=1, login_style=1):
def update_header(file_path, sheet_name, host, caseno):

    """
    :param file_path:
    :param sheet_name:
    :param host:
    :param caseno:
    :return:
    """
    file = open_xlsx(file_path)
    original_sheet = file.sheet_by_name(sheet_name)  # 通过名称获取
    content = read_xlsx(original_sheet, host, caseno)
    is_update = content["Test_Update"]  # 是否更新信息头
    case_no = content["Test_Number"]  # 用例id
    login_data= content["Test_AccountPassword"] # 登录数据

    #  获取数据所在的行
    position = Excel_Manage.Excel_DataPosition()
    get_position = position.excel_dataposition(file_path, sheet_name, case_no)
    line = get_position[0]  # 行位置

    if is_update == "是":
        # account_password = content["Test_AccountPassword"]  # 账号密码

        username = login_data["username"]
        password = login_data["password"]
        if "system" in login_data.keys():
            system = login_data["system"]
        else:
            system = 1
        if "login_style" in login_data.keys():
            login_style = login_data["login_style"]
        else:
            login_style = 1

        account_password = {
            "username": username,
            "password": password
        }
        # print(account_password)

        new_header = Business_Package.updata_header(host, config.headers, account_password, system, login_style)

        #  修改用例中的header
        #  print("新信息头为：%s" % new_header)
        excel_xl = Excel_Manage.excelprocess_xl()
        excel_xl.write_excel_xls_modify(file_path, line, 8, new_header, sheet_name=sheet_name, style=1)
        # print("header修改成功")
        return True, new_header, line
    else:
        # print("header保持不变")
        return False


# 请求接口
def requet_xlsx(content):
    """
    :param content:
    :return:
    """
    headers = content["Test_Headers"]
    urls = content["Test_Url"]
    request_method = content["Test_Method"]
    test_name = content["Test_Name"]
    test_no = content["Test_Number"]
    try:
        print("\n测试场景为：\n%s：%s" % (test_no, test_name))
        print("\n请求地址：\n%s" % urls)
        print("\n请求头：\n%s" % headers)

        # 根据不同的请求方式，发出对应请求
        # 请求方式统一格式
        new_request_method = request_method.upper()

        # 判断是否需要header，判断请求参数格式转换
        if headers:
            new_headers = headers
            datas = json.dumps(content["Test_Data"])
        else:
            new_headers = config.headers
            datas = content["Test_Data"]
        print("\n请求参数：\n%s" % datas.encode('utf-8').decode('unicode_escape'))

        # # 调用接口
        # interface_request = requests.request(new_request_method, url=urls, data=datas, headers=new_headers, verify=False)
        # response = json.loads(interface_request.text)  # json.loads()用于将字符串形式的数据转化为字典
        # print("\n响应数据：\n%s" % response)
        # return response
        urllib3.disable_warnings()
        if new_request_method == "POST":
            interface_request = requests.request(new_request_method, url=urls, data=datas, headers=new_headers, verify=False)
        elif new_request_method == "GET":
            new_datas = content["Test_Data"]
            new_url = urls + "/%s" % (new_datas["uid"])
            print(new_url)
            interface_request = requests.request(new_request_method, url=new_url, headers=new_headers, verify=False)
        elif new_request_method == "DELETE":
            interface_request = requests.request(new_request_method, url=urls, data=datas, headers=new_headers, verify=False)
        elif new_request_method == "PUT":
            interface_request = requests.request(new_request_method, url=urls, data=datas, headers=new_headers, verify=False)

        response = json.loads(interface_request.text)  # json.loads()用于将字符串形式的数据转化为字典
        print("\n响应数据：\n%s" % response)
        return response

    except Exception as errs:
        logging.exception("出现问题")
        raise errs



# 执行用例
def run_xlsx(file_path, sheet_name, row_name, host, host_chome=config.test_url_chome):  # 参数：文件，表名称，行名称，网址
    """
    :param file_path:
    :param sheet_name:
    :param row_name:
    :param host:
    :param host_chome:
    :return:
    """

    update_header(file_path, sheet_name, host, row_name)  # 更新header

    file = open_xlsx(file_path)  # 打开excel
    #  获取文件的具体表
    #  sheet_names = original_file.sheet_names() #  获取所有表名
    #  print(sheet_names)
    original_sheet = file.sheet_by_name(sheet_name)  # 通过名称获取
    content = read_xlsx(original_sheet, host, row_name)  # 获取用例并且参数化
    result = requet_xlsx(content)  # 请求接口
    # print(result)

    #  获取匹配方式，并且转为int类型
    if isinstance(content["Match_Type"], int):
        Match_Type = content["Match_Type"]
    else:
        Match_Type = int(content["Match_Type"])

    check = []
    if Match_Type == 1:
        if content["Test_Except"]:
            Except_data = json.loads(content["Test_Except"])
            print("\n循环检查点为：%s" % Except_data)
            loop_check = Json_data.json_check(result, content["Test_Except"])
            # print(loop_check)
            if False not in loop_check:
                check.append(True)
            else:
                check.append(False)
        else:
            print("\n循环检查点的值为空，请录入检查值")
            check.append(False)

    elif Match_Type == 2:
        if content["Path_Except"]:
            path = eval(content["Path_Except"].split("#")[0])  # eval返回字符串值
            value = eval(content["Path_Except"].split("#")[1])
            print("\n路径检查点为：路径为%s，值为%s" % (path, value))
            path_check = Json_data.json_path(result, path, value)
            #  print(path_check)
            if path_check[0] == [True]:
                check.append(True)
            else:
                check.append(False)
        else:
            print("\n路径检查点的值为空，请录入检查值")
            check.append(False)
    else:
        try:
            if content["Test_Except"]:
                Except_data = json.loads(content["Test_Except"])
                print("\n循环检查点为：%s" % Except_data)
                loop_check = Json_data.json_check(result, content["Test_Except"])
                #  print(loop_check)
            else:
                loop_check = [False]
                print("\n循环检查点的值为空，请录入检查值")
        except Exception as errs:
            logging.exception("出现问题")
            raise errs

        try:
            if content["Path_Except"]:
                path = eval(content["Path_Except"].split("#")[0])
                value = eval(content["Path_Except"].split("#")[1])
                print("\n路径检查点为：路径为%s，值为%s" % (path, value))
                path_check = Json_data.json_path(result, path, value)
            else:
                path_check = [[False]]
                print("\n路径检查点的值为空，请录入检查值")
        except Exception as errs:
            logging.exception("出现问题")
            raise errs

        if False not in loop_check and path_check[0][0] == True:
            check.append(True)
        else:
            check.append(False)

        # print(check)
    if False not in check:
        return True, result
    else:
        return False, result


if __name__ == "__main__":
    file_path1 = "../../接口测试用例-魏奇.xlsx"
    sheet_name2 = "normal_order_create"
    case_no3 = "custom_order_case_04"
    sheet_name1 = "custom_order"
    case_no1 = "custom_order_case_24"
    case_no2 = "custom_order_case_14"
    host_chome1 = config.test_url_chome
    host_cloud1 = config.test_url_mall

    #  result1 = run_xlsx(file_path1, sheet_name1, case_no3, host_cloud1)
    #  result2 = run_xlsx(file_path1, sheet_name1, case_no1, host_cloud1)
    result3 = run_xlsx(file_path1, sheet_name1, case_no2, host_cloud1)
