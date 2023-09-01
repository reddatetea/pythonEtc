# encoding=utf-8
import sys

path1 = sys.path[0]  # 当前项目路径
path2 = sys.base_exec_prefix  # Python的安装路径
if path1[0:1] == path2[0:1]:
    print("项目与Python都在", path1[0:1], "磁盘里")
else:
    print("项目文件在", path1[0:1], "盘，Python被安装在", path2[0:1], "盘")
