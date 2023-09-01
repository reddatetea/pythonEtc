#encoding=utf-8
import sys
encoding1 = sys.getfilesystemencoding()  # 获取本地文件编码格式
if encoding1 == "utf-8":                 # 判断编码格式是否为utf-8
    print("没错，你的本地文件编码格式就是", encoding1)
else:
    print("不，你的本地文件编码格式不是utf-8")


