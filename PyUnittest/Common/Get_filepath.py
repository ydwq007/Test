# -*- coding: utf-8 -*-
"""
接口：获取指定路径下的文件或文件夹
创建人：魏奇
更新人：魏奇
更新时间：2020-02-01 11:29
描述：
"""

import os,sys

def all_filepath(dir):

    folder = []
    folderpath = []
    file = []
    filepath = []
    # os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
    for root,subdirs,filenames in os.walk(dir):
        # print("当前主目录为：%s" % root)
        # print("当前主目录下的所有目录为：%s" % subdir)
        # print("当前主目录下的所有文件为：%s" % filenames)
        for filename in filenames:
            remove_file = "cpython"
            if remove_file not in filename:
                file.append(filename)
                fpath = os.path.join(root, filename)#合并成一个完整路径
                filepath.append(fpath)
        for subdir in subdirs:
            remove_folder = "pycache"
            if remove_folder not in subdir:
                folder.append(subdir)
                spath = os.path.join(root,subdir)
                folderpath.append(spath)

    folder_list = zip(folder,folderpath)
    file_list = zip(file,filepath)

    # 打印结果
    n,m = 1,1
    print("\n指定目录下包含目录共%s个" % len(folder))
    for i in range(len(folder)):
        print("第%s个目录，名称为%s，路径为%s" % (n,folder[n-1],folderpath[n-1].replace("\\","/")))
        n += 1
    print("\n指定目录下包含文件共%s个" % len(file))
    for j in range(len(file)):
        print("第%s个文件，名称为%s，路径为%s" % (m,file[m-1],filepath[m-1].replace("\\","/")))
        # print(type(filepath[m-1]))
        m += 1

    return dir,folder,folderpath,file,filepath,folder_list,file_list

if __name__ == "__main__":
    path = "../TestCases"
    path1 = r"..\TestCases"
    path2 = "..\\TestResults"
    all_filepath(path2)
