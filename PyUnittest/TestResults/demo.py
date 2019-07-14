# import sys
# sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\Common") #跨目录调用需要配置路径,接口路径
# import SendEmail
#
# SendEmail.sendemail(2,2)


# import time
#
# a = time.time()
# b = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# c = time.time.now()
# print(a)
# print(b)
# print(c)
import time
content = "ruiewriuyriuywquiryrwqiryqyriqyr"
d = "test_result %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
with open(r"D:\IdeaProjects\seeyon\PyUnittest\TestResults\test_result.txt", "w") as result_html: #测试报告路径
    result_html.write(content)

import os
a = r"D:\IdeaProjects\seeyon\PyUnittest\TestResults\test_result.txt"
b = r"D:\IdeaProjects\seeyon\PyUnittest\TestResults\%s.txt" % d
os.rename(a,b)

# import os
# path =r"D:\IdeaProjects\seeyon\PyUnittest\TestResults\test_result.txt"
# for file in os.listdir(path):
#     name = file.split('.')[0]
#     os.rename(os.path.join(path, file), os.path.join(path, '%05d' % int(name) + ".txt"))