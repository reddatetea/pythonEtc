import sys
version = sys.version#获取Python解释器的版本号等信息
index1 = version.index(",")#获取第一个逗号的索引
index2 = version.index(")")#获取第一个右小括号的索引
print(version[index1+2:index2])#截取日期部分的字符串