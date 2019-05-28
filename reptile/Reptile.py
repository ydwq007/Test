#爬虫12306网址
import re,requests,logging,json
from colorama import Fore #导入字体颜色
from bson import json_util
logging.basicConfig(level=logging.DEBUG)
import prettytable  #导入ASCII格式的表格
from stations import chezhan_names,chezhan_code


#定义参数
train_date = "2019-06-07"
from_station = "BJP"
to_station = "SHH"

#请求地址
# url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-06-07&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT"
url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s" \
      "&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT" % (train_date,from_station,to_station)
print(url)


#verify=False 跳过认证。requests.get(url,parmar,verify)
responses = requests.get(url,verify=False)

#利用re正则，获取车站的名字和编码
# datas = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', responses.text) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文
datas = responses.text

#打印结果
print(datas)
print(json_util.dumps(datas,ensure_ascii=False,indent=4)) #打印响应结果，以json格式输出

data1 = json.loads(datas)

print("打印data1的值为%s" % data1)
print(type(data1))

print(data1["data"]["result"])
#引入prettytable，创建表格
table = prettytable.PrettyTable(["车次","出发站","到达站","出发时间","到达时间","历时","商务座和特等座","一等座","二等座","高级软卧","软卧一等卧","动卧","硬卧二等卧","软座","硬座","无座","其他","备注"])

#从返回数据的关键字为result的值获取数据
for i in data1["data"]["result"]:
    #创建一个列表
    name = [
        "station_train_code", #车次
        "from_station_name", #出发站
        "to_station_name", #到达站
        "start_time", #出发时间
        "arrive_time", #到达时间
        "lishi", #历时
        "swz_num", #商务座和特等座
        "ydz_num", #一等座
        "edz_num", #二等座
        "gjrw_num", #高级软卧
        "ydrw_num", #软卧一等卧
        "dw_num", #动卧
        "yw_num", #硬卧二等卧
        "rz_num", #软座
        "yz_num", #硬座
        "wz_num", #w无座
        "qt_num", #其他
        "note" #备注

    ]
    #创建key:value的字典
    value = {
        "station_train_code":"", #车次
        "from_station_name":"", #出发站
        "to_station_name":"", #到达站
        "start_time":"",#出发时间
        "arrive_time":"", #到达时间
        "lishi":"", #历时
        "swz_num":"",#商务座和特等座
        "ydz_num":"",#一等座
        "edz_num":"", #二等座
        "gjrw_num":"",#高级软卧
        "ydrw_num":"", #软卧一等卧
        "dw_num":"", #动卧
        "yw_num":"", #硬卧二等卧
        "rz_num":"", #软座
        "yz_num":"", #硬座
        "wz_num":"", #w无座
        "qt_num":"", #其他
        "note":"" #备注
    }
    #赋值
    item = i.split("|") #使用split方法用"|"分割数据
    value["station_train_code"] = item[3]                          #车次在3号位置
    value["from_station_name"] = item[4]                           #出发站在4,6号位置
    value["to_station_name"] = item[5]                             #到达站在5,7号位置
    value["start_time"] = item[8]                                  #出发时间在8号位置
    value["arrive_time"] = item[9]                                 #到达时间在9号位置
    value["lishi"] = item[10]                                      #历时在10号位置
    value["swz_num"] = item[32] or item[25]                        #商务座和特等座在32或25号位置
    value["ydz_num"] = item[31]                                    #一等座在31号位置
    value["edz_num"] = item[30]                                    #二等座在30号位置
    value["gjrw_num"] = item[21]                                   #高级软卧在21号位置
    value["ydrw_num"] = item[23]                                   #软卧一等卧在23号位置--
    value["dw_num"] = item[27]                                     #动卧在27号位置
    value["yw_num"] = item[28]                                     #硬卧二等卧在28号位置
    value["rz_num"] = item[24]                                     #软座在24号位置
    value["yz_num"] = item[29]                                     #硬座在29号位置
    value["wz_num"] = item[26]                                     #w无座在26号位置
    value["qt_num"] = item[22]                                     #其他在22号位置
    value["note"] = item[1]                                        #备注在1号位置

    #值为空的展示
    for pos in name:
        if value[pos] == "":
            value[pos] = "-"

    #向表格里添加数据
    tickets = []

    #先循环数据的条数，在循环每条数据的值
    count = [] #条数
    count.append(value)
    for x in count:
        table1 = []
        for y in name:
            if y == "station_train_code":
                s = value["station_train_code"]
                table1.append(s)
            #出发站点转换为汉字
            elif y == "from_station_name":
                s = chezhan_names[value["from_station_name"]]
                table1.append(s)
            #出发站点转换为汉字
            elif y == "to_station_name":
                s = chezhan_names[value["to_station_name"]]
                table1.append(s)
            else:
                table1.append(value[y])
        tickets.append(table1)

    for ticket in tickets:
        table.add_row(ticket)

#打印表格
print(table)






