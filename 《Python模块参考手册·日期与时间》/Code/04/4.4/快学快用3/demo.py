import time                         #导入time模块
t=(2020,5,20,21,36,54,3,347,0)     #创建一个名称为t的时间元组
#根据提供的时间元组获取年-月-日 时:分:秒
print(time.strftime('%Y-%m-%d %H:%M:%S',t))
#根据localtime()返回的时间获取年 月 日 时 分 秒
print(time.strftime('%Y %m %d %H %M %S',time.localtime()))
#根据gmtime()返回的时间获取年,月,日 时:分:秒
print(time.strftime('%Y,%m,%d %H:%M:%S',time.gmtime()))
