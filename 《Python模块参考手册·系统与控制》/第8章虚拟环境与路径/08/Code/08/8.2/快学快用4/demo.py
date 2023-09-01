#encoding=utf-8
import sys, os
for i in sys.path:  # 遍历所有路径
    it = i.split("\\")  # 将路径以\分割
    filename = it[len(it) - 1]  # 分割后的最后一个字符串
    if len(filename.split(".")) <= 1:  # 判断最后一个字符串判断该路径是文件还是文件夹
        print(i)

