import os  # 文件与操作系统相关模块
for i in range(1,10):# 遍历1~10数字
    if i==8:# 到数字8时
        os._exit(1)# 跳出程序，不再执行程序
    print(i)  # 输出结果
