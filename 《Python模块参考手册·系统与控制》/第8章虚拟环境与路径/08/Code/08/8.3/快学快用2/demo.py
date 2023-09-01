# encoding=utf-8
import sys

print('Python安装目录：' + sys.base_exec_prefix)
if sys.base_exec_prefix[0:1] == 'C':  # 判断是否安装在C盘
    print('Python安装在系统盘 C 盘中，请谨慎！')
else:
    print('Python没有安装在系统盘 C 盘中，这个习惯不错哦！')
