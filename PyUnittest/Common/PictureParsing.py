# -*- coding: utf-8 -*-
"""
接口：图片解析
创建人：魏奇
更新人：魏奇
更新时间：2019-09-30 9:45
描述：从验证码图片获取验证码
"""

from PIL import Image #从 Pillow 中导入图片处理模块 Image
import pytesseract # 导入基于 Tesseract 的文字识别模块 pytesseract
import re,requests,base64,os

#安装Tesseract-OCR
#下载地址：http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe
#环境配置：
#1. 将Tesseract-OCR安装目录加入环境变量path中
#2. 新建环境变量TESSDATA_PREFIX，值为Tesseract-OCR安装目录下的tessdata，如C:\Program Files (x86)\Tesseract-OCR\tessdata
#3. 更改pytesseract.py的tesseract_cmd，值为Tesseract-OCR.exe的路径，如tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
#4. 重启

# image = Image.open(r"D:\apache-jmeter-5.1.1\demo\ZY\6067.png")
# code = pytesseract.image_to_string(image)
# print(code)

#保存验证图片
def save_picture(url,path):#参数为图片URL

    #获取响应结果
    response = requests.get(url,verify=False)

    #打印结果
    # print(response.content)
    # print(type(response.content))

    #bytes字节串转string字符串
    str = response.content.decode("utf-8","ignore") # 第一参数默认utf8，第二参数默认strict
    # print(str)

    #保存图片
    #针对返回的不仅仅含有图片base64加密内容
    if "code" in str:
        content = str[43:-2]
        # print(content)
        # with open("../TestResults/Picture/save_picture/save_picture_1.png","wb") as picture:
        with open(path,"wb") as picture:
            picture.write(base64.b64decode(content))
    #针对返回的仅含有图片base64加密内容
    else:
        # with open("../TestResults/Picture/save_picture/save_picture_2.png","wb") as picture:
        with open(path,"wb") as picture:
            picture.write(response.content)

#保存base64加密图片
def base_64(img_base64):#参数为base64加密字符串
    img_bin = base64.b64decode(img_base64)
    with open('../TestResults/Picture/base_64.png', 'wb') as f:
        f.write(img_bin)

#获取验证数据
def get_verification_data(path):#参数为图片地址

    image = Image.open(path) # 打开验证码图片文件
    im = image.convert("L") # 基本处理，灰度处理，提升识别准确率
    im.save("../TestResults/Picture/demo001.png")  # 保存处理后的图片
    # 利用pytesseract进行图片内容识别
    text = pytesseract.image_to_string(im,lang="chi_sim") #lang="chi_sim"使用中文解析图片
    # 去除识别结果中的非数字/字母内容
    text = re.sub("\W", "", text) #返回类型为str,\W等同于[^0-9a-zA-Z]
    # print(type(text))
    if len(text.strip()) == 0:
        print("未识别到结果")
        return text,False
    else:# 返回验证码内容
        print("识别结果为：%s" % text)
        return text,True


def discern(path,url):#参数为图片地址

    picture,t,f,result = [],[],[],[]
    for file in os.listdir(path):
        if file.endswith('.png') or file.endswith('.jpg'):
            picture.append(file)
    length = len(picture)

    for i in range(length):
        picture_path = path+picture[i]
        print("\n当前识别第%s张图片" % (i+1))
        print("当前识别图片路径为：%s" % picture_path)

        j,c = 0,10   # 当前次数和总共次数
        captcha = get_verification_data(picture_path) #获取验证吗
        # print(captcha[1])
        # 基本检验，验证码位数必须为四位
        while j < c:
            # if len(captcha) != 0:
            if captcha[1] == False:
                # captcha = get_verification_data(data)
                j = j + 1
                if j == c:
                    print("同一图形识别次数已达上限：%s次，识别失败" % c)
                    f.append(picture[i]) #图片名称
                else:
                    print("第%d次识别错误，还剩下%s次机会" % (j,(c-j)))
                    captcha = get_verification_data(picture_path)
                save_picture(url,picture_path)
            else:
                print("第%d次识别成功" % (j+1))
                t.append(picture[i]) #图片名称
                result.append(captcha[0])
                break

    print("\n共识别%s张图片，其中成功%s张，失败%s张" % (length,len(t),len(f)))
    print("识别成功的图片和结果为：\n")
    for u in range(len(t)):
        print("【%s：%s】" % (t[u],result[u]))
    print("识别失败的图片为：%s" % f)



#执行识别图片
if __name__ == "__main__":


    #识别图片
    path = "../TestResults/Picture/save_picture/"
    url = "https://testchome.seeyon.com/portal.php?m=util&a=randcode&type=login&w=90&h=40&base64=1"
    discern(path,url)



    # #保存图片
    # url = "https://testchome.seeyon.com/portal.php"
    # url1 = "http://img.ivsky.com/img/tupian/pre/201708/30/kekeersitao-002.jpg"
    # url2 = "https://testchome.seeyon.com/portal.php?m=util&a=randcode&type=login&w=90&h=40&base64=1"
    # save_picture(url1)
    # save_picture(url2)

    # #base64
    # base64_data = "iVBORw0KGgoAAAANSUhEUgAAAFoAAAAoBAMAAACMbPD7AAAALVBMVEXz+\\/5CNHLGydvc4uyEfqZYTIOal7hu" \
    #          "ZZWwsMl5cZ1oX5BdUodaT4WUkbPIzNxcsuShAAABbUlEQVQ4jdWSMU\\/CQBiGj7sKjLzYo5o4YCRxcKmWBMcSg" \
    #          "6yUkMhIB+JmPEicqYPxb\\/ij\\/D9+d1VsvcbSuMg7XK9fnn73fm+Psf2R8CvAvcjdHXYAdHeFeTTvF9M8X+1pv" \
    #          "6cu43LkWWxwNcQ0Wxi6PuMIRYO8LH7SMRUP845d\\/wB+EnkK4Vexhm9N0lLTrNTz+A038HwHm20PZGUqyex+zdg" \
    #          "lZtpD4rGGtIesf37QYufGaYzNBU5CJ2Rx26YdHWzqS+oREpyJd8igWy+KkHz6WWs8worFMlqpqQ1T2629KOWXWCcd" \
    #          "0Jh256cY6YUQrAm0xdJYCh4gNxZMCVCTZ5PIgvYhBx5piAm3\\/wypOdat9E5JpTdKhwyI1+ILK16UsaKTPKKboDq" \
    #          "+HqCQNQrMOiAT+jR4I3i1X\\/BUCeb60adD2qzWKqHFML0Y1+NbMl2K87vsG0q7595K8bxKJ\\/0LXp5jHq9mvSK+" \
    #          "z8FUxCvR\\/0gftqkxQDVNz1EAAAAASUVORK5CYII="
    # base_64(base64_data)




