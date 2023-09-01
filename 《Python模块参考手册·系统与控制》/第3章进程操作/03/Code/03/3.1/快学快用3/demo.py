import os  # 文件与操作系统相关模块
times = os.times()  # 返回当前的全局进程时间
if times.system<1:# 判断用户时间
     print('系统时间是：',times.system,'好系统，跑得快')# 速度在0~1秒之间，提示信息
else:# 否则
    print('你是胖猪嘛，这么慢')#提示信息速度慢
