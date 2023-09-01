#encoding=utf-8
import sys
path1=sys.path         #获取Python解释器的模块中文件夹的路径
for it in path1:       #遍历路径
    if it.count("pip")>0:    #判断路径中是否含有字符串"pip"
        print(it)        #输出路径

