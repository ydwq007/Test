# -*- coding: utf-8 -*-
"""
接口：通过读取excel的数据，执行用例
创建人：魏奇
更新人：魏奇
更新时间：2019-12-18 20:57
描述：通过读取excel的数据，执行用例
"""
import xlrd,requests,json,sys
sys.path.append("./Common") #跨目录调用需要配置路径
import Json_data,Data_Structure,Excel_Manage
sys.path.append("../TestDatas")
import config

#打开用例文件
def open_xlsx(filepath):

    file = xlrd.open_workbook(filepath)
    return file

#读取用文件，将结果参数化
def read_xlsx(sheet,host,caseno):

    case_no = sheet.col_values(0)   #返回用例编号列的所有值为列表
    # print(case_no)
    # 获取用例编号所在的行
    try:
        row = case_no.index(caseno)
        print(row)
    except Exception as err:
        print("用例编号%s未找到" % caseno)
        raise

    content = {}  #初始化字典
    content["Test_Number"] = sheet.cell_value(row,0)  #用例编号
    content["Test_Name"] = sheet.cell_value(row,1)    #场景名称
    content["Test_Url"] = host + sheet.cell_value(row,2)      #接口URL

    content["Test_Update"] = sheet.cell_value(row,3) #是否更新信息头（是,否）
    content["Test_AccountType"] = sheet.cell_value(row,4) #账号类型（A,B）
    content["Test_AccountPassword"] = json.loads(sheet.cell_value(row,5)) #账号密码

    content["Test_Method"] = sheet.cell_value(row,6)  #接口请求方法
    # content["Test_Headers"] = json.loads(sheet.cell_value(row,7))  #接口请求头,转为为字典

    headers = sheet.cell_value(row,7) # 获取信息头
    if headers:
        content["Test_Headers"] = json.loads(headers)  #接口请求头,转为为字典
    else:
        content["Test_Headers"] = config.headers
    content["Test_Data"] = json.loads(sheet.cell_value(row, 8))    #接口入参,转为为字典
    # print(type(content["Test_Data"]))
    content["Test_Except"] = sheet.cell_value(row,9)   #接口预期值
    content["Test_Code"] = sheet.cell_value(row,10)   #接口响应码

    return content

# 更新信息头
def update_header(file_path,sheet_name,host,caseno):

    file = open_xlsx(file_path)
    original_sheet = file.sheet_by_name(sheet_name) #通过名称获取
    content = read_xlsx(original_sheet,host,caseno)
    is_update = content["Test_Update"] # 是否更新信息头
    case_no = content["Test_Number"] # 用例id

    # 获取数据所在的行
    position = Excel_Manage.Excel_DataPosition()
    get_position = position.excel_dataposition(file_path,sheet_name,case_no)
    line = get_position[0] # 行位置
    if is_update == "是":
        # 登录或token，更改header信息
        account_type = content["Test_AccountType"]  # 账号类型
        account_password = content["Test_AccountPassword"] # 账号密码

        # 信息头
        headers = {
            "Content-Type": "application/json",
            "Connection":"keep-alive"
        }
        # A类账号登录参数
        aloneA = {
            "m": "LoginCloud",
            "a": "login",
            "account_type": 1,
            "username": account_password["username"],
            "password": account_password["password"]
        }
        # B类账号登录参数
        dealer = {
            "m": "LoginCloud",
            "a": "login",
            "account_type": 2,
            "username": account_password["username"],
            "password": account_password["password"]
        }

        if account_type == "A" or account_type == "a":
            Auserlogin = Data_Structure.get_token(host,aloneA,headers) # A账号登录云商前台
            new_header = Auserlogin[2]

        elif account_type == "B" or account_type == "b":
            Buserlogin = Data_Structure.get_token(host,dealer,headers)# B账号登录云商前台
            new_header = Buserlogin[4]

        elif account_type == "Badmin" or account_type == "badmin":
            Badminuserlogin = Data_Structure.get_mallid(host,config.test_url_mall,dealer,headers)# B账号登录云商后台
            new_header = Badminuserlogin[2]

        # 修改用例中的header
        # print("新信息头为：%s" % new_header)
        excel_xl = Excel_Manage.excelprocess_xl()
        excel_xl.write_excel_xls_modify(file_path,line,8,new_header,sheet_name=sheet_name,style=1)
        print("header修改成功")
        return new_header,line
    else:
        print("header保持不变")

#请求接口
def requet_xlsx(content):

    headers = content["Test_Headers"]
    urls = content["Test_Url"]
    request_method = content["Test_Method"]
    try:
        print("\n请求地址：\n%s" % urls)
        print("\n请求头：\n%s" % headers)
        #根据不同的请求方式发出http请求
        if request_method == "post" or request_method == "POST":
            #判断请求头是否有参数
            if headers:
                contenttype = headers["Content-Type"]
                if contenttype == "application/json":
                    datas = json.dumps(content["Test_Data"])
                    print("\n请求参数：\n%s" % datas.encode('utf-8').decode('unicode_escape'))
                    interface_request = requests.post(url=urls,data=datas,headers=headers,verify=False)
                    response = json.loads(interface_request.text) #json.loads()用于将字符串形式的数据转化为字典
                elif contenttype == "multipart/form-data":
                    datas = content["Test_Data"]
                    print("\n请求参数：\n%s" % datas.encode('utf-8').decode('unicode_escape'))
                    interface_request = requests.post(url=urls,files=datas,headers=headers,verify=False)
                    response = json.loads(interface_request.text) #json.loads()用于将字符串形式的数据转化为字典
            else:
                new_headers = config.headers
                datas = content["Test_Data"]
                interface_request = requests.post(url=urls,data=datas,header=new_headers,verify=False)
                response = json.loads(interface_request.text) #json.loads()用于将字符串形式的数据转化为字典
            print("\n响应数据：\n%s" % response)
        elif request_method == "get" or request_method == "GET":
            #判断请求头是否有参数
            if headers:
                datas = json.dumps(content["Test_Data"])
                print("\n请求参数：\n%s" % datas.encode('utf-8').decode('unicode_escape'))
                interface_request = requests.get(url=urls,data=datas,headers=headers,verify=False)
                response = json.loads(interface_request.text) #json.loads()用于将字符串形式的数据转化为字典
                print("\n请求头：\n%s" % headers)
            else:
                datas = content["Test_Data"]
                print("\n请求参数：\n%s" % datas.encode('utf-8').decode('unicode_escape'))
                interface_request = requests.post(url=urls,data=datas,verify=False)
                response = json.loads(interface_request.text) #json.loads()用于将字符串形式的数据转化为字典
            print("\n响应数据：\n%s" % response)
        else:
            print("\n请求方式未定义：%s" % content["Test_Method"])
        return response
    except Exception as err:
        print("\n请求异常，结果如下：\n%s" % err)
        raise

# 执行xlsx用例
def run_xlsx(original_file,sheet): #参数：文件，表顺序

    original_sheet = original_file.sheets()[sheet] #通过索引顺序获取
    count = original_sheet.nrows #总计行数
    for i in range(1, count):
        content = read_xlsx(original_sheet,i)
        result = requet_xlsx(content)


def run_xlsx1(file_path,sheet_name,row_name,host,host_chome=config.test_url_chome): #参数：文件，表名称，行名称，网址

    update_header(file_path,sheet_name,host_chome,row_name) # 更新header

    file = open_xlsx(file_path) # 打开excel
    # 获取文件的具体表
    # sheet_names = original_file.sheet_names() # 获取所有表名
    # print(sheet_names)
    original_sheet = file.sheet_by_name(sheet_name) #通过名称获取
    content = read_xlsx(original_sheet,host,row_name) # 获取用例并且参数化
    result = requet_xlsx(content) # 请求接口
    # print(result)

    # 获取实际响应码，并且转换为int类型
    if isinstance(result["code"],int):
        Actual_Code = result["code"]
    else:
        Actual_Code = int(result["code"])

    # 获取期望响应码，并且转换为int类型
    if isinstance(content["Test_Code"],int):
        Except_Code = content["Test_Code"]
    else:
        Except_Code = int(content["Test_Code"])

    #获取期望关键字和值
    Except = json.loads(content["Test_Except"])
    print("\n检查点为：%s" % Except)

    # 判断响应码
    sign = []
    if Actual_Code == Except_Code:
        print("进入检查点")
        #key和value校对
        count = 1
        for key in Except.keys():
            check = Json_data.json_check(result,key,Except[key]) #key和value校对
            # print(check)
            if check == True:
                print("第%s检查点，检查成功。key为%s，期望值为%s" % (count,key,Except[key]))
                sign.append(True)
            else:
                print("第%s检查点，检查失败。key为%s，期望值为%s" % (count,key,Except[key]))
                sign.append(False)
            count += 1
        if sign and False not in sign:
             return True,result
        else:
            return False,result
            # # 判断期望值
        #     print(Except.keys())
        #     for key in Except.keys():
        #         print(key)
        #         print(Except[key])
        #         check = Json_data.json_check(result,key,Except[key])
        #         if check == True:
        #             print("检查成功。key为%s，值为%s" % (key,Except[key]))
        #             sign.append(True)
        #     print(sign)
        #     if False not in sign:
        #         return True
        #     else:
        #         return False
    else:
        print("\n未进入检查点")
        return False,result


if __name__ == "__main__":

    file_path = "../../Experiment/Other/接口测试用例-魏奇.xlsx"
    sheetname = "normal_order_create"
    caseno = "normal_order_create_case_01"
    sheetname1 = "normal_order_procedure"
    caseno1 = "normal_order_procedure_case_07"
    # host_chome = "https://testchome.seeyon.com"
    host_cloud = "https://testcloud.seeyon.com"

    result1 = run_xlsx1(file_path,sheetname,caseno,host_cloud)
    result1 = run_xlsx1(file_path,sheetname1,caseno1,host_cloud)
