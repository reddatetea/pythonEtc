import sys
hexversion = hex(sys.hexversion)#Python版本号的十六进制表示形式
major = hexversion[2]#获取主版本号
minor = hexversion[4]#获取次版本号
micro = hexversion[6]#获取生成号
#输出当前使用的Python版本号
print("当前使用的Python版本号：{:s}.{:s}.{:s}".format(major,minor,micro))