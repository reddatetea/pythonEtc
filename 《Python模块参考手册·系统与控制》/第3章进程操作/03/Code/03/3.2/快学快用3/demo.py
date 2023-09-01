import os
try:
    f=open('test.txt','r')#打开文件
    line = f.readline()#读取文件一行内容
    print(line)#输出一行内容
    os._exit(0)#退出程序
except Exception :
   print('到此结束')#提示信息
   f.close()#关闭文件
