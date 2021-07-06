# -*- coding: utf-8 -*-
"""
接口：将指定路径下的文件复制到指定路径下
创建人：魏奇
创建时间：2020-02-02 15:08
描述：
"""

import os
import shutil


# 创建保存文件的文件夹
def CreateFolder(path):
    """
    :param path:
    """
    isexit = os.path.exists(path)
    if isexit:
        print("目标文件夹已存在：%s" % path)
    else:
        os.makedirs(path)
        print("目标文件夹创建成功：%s" % path)

# 复制文件
def FileCopy(filepath, newpath):  # 源路径，目标路径
    """
    :param filepath:
    :param newpath:
    """
    isexit1 = os.path.exists(filepath)
    isexit2 = os.path.exists(newpath)
    remove_file = "cpython"
    remove_folder = "pycache"

    if isexit1:
        if isexit2:
            # 获取指定路径下的文件
            filenames = os.listdir(filepath)
            for filename in filenames:
                newdir = filepath + "/" + filename
                # 判断是否为文件
                if os.path.isfile(newdir) and remove_file not in filename:
                    print(newdir)
                    newfile = newpath + filename
                    shutil.copyfile(newdir, newfile)
                else:
                    if remove_folder not in filename:
                        FileCopy(newdir, newpath)
        else:
            print("目标路径不存在：%s" % newpath)
    else:
        print("源路径不存在：%s" % filepath)


def Filedel(path):
    """
    :param path:
    """
    # 判断路径是否存在
    isexit = os.path.exists(path)
    if isexit:
        if os.path.isfile(path):
            os.remove(path)
            print("目标为文件类型，删除成功：%s" % path)
        else:
            shutil.rmtree(path, True)  # 删除文件夹及其内部所有文件夹和文件
            print("目标为文件夹类型，删除成功：%s" % path)
    else:
        print("路径不存在：%s" % path)


if __name__ == "__main__":
    oldpath = "../../TestCases"
    newpath = "../Copy/"
    CreateFolder(newpath)
    FileCopy(oldpath,newpath)
    Filedel("../Copy/")

