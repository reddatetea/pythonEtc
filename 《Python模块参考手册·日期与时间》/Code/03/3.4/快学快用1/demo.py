import time           # 导入time模块
def procedure():      # 执行函数
 a = 0             # 定义变量
 for i in range(1000000):   # 循环
     a+=i                    # 循环增加变量
     print(a)                # 打印机当前变量值
start_time = time.perf_counter()       # 第一次调用perf_counter()方法
procedure()                     # 调用循环增加变量的函数
print('函数的运行时间为：',time.perf_counter()-start_time,'秒')  # 打印函数运行的时间
