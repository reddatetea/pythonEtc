import os  # 文件与操作系统相关模块
times = os.times()  # 返回当前的全局进程时间
if 0 < times.user < 1:  # 判断用户时间
     print('用户时间：',times.user,'速度挺快哟，赞赞赞')  # 速度在0~1秒之间，提示信息
else:  
     print('速度太慢了，等到花儿都谢了')  # 提示信息速度慢
