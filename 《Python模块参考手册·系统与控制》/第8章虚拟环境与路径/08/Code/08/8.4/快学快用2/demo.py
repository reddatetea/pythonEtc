#encoding=utf-8
import sys
import os  # 需要使用os模块的listdir()方法遍历文件夹
path1 = sys.prefix  # 获取虚拟路径
path = path1.replace("\\", "/")  # 将路径中的\替换为/
print("该路径的子文件夹数量为", len(os.listdir(path)))
