#encoding=utf-8
import sys
print('文件系统原编码名称：', sys.getfilesystemencoding())  # 输出文件系统编码
print('文件名原转换错误模式：', sys.getfilesystemencodeerrors())  # 输出文件名转换时的错误模式名称
sys._enablelegacywindowsfsencoding()  # 改变默认文件系统编码和错误模式
print('改变后的文件系统编码名称：', sys.getfilesystemencoding())  # 输出文件系统编码
# 输出文件名转换时的错误模式名称
print('改变后的文件名转换错误模式：', sys.getfilesystemencodeerrors())

