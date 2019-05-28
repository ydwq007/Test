#获取火车的站台数据

import requests,re
from bson import json_util

#请求的地址
url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9100"

#verify=False 跳过认证。requests.get(url,parmar,verify)
result = requests.get(url,verify=False)

#利用re正则，获取车站的名字和编码
chezhan = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', result.text) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文
chezhan_code = dict(chezhan) #组成字典

#进行交换
chezhan_names = dict(zip(chezhan_code.values(),chezhan_code.keys()))
#打印出得到的车站字典
#print(chezhan_names)
print(json_util.dumps(chezhan_names,ensure_ascii=False,indent=4)) #打印响应结果，以json格式输出

