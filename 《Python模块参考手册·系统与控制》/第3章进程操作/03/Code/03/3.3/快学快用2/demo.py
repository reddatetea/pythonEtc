import os  # 文件与操作系统相关模块
while True:
    i=int(input("请输入数字："))# 输入数字
    if i==3:# 输入数字是3
        os.abort()#请求异常终止信号
        print("请求异常终止信号")
    else:# 输入数字不是3
        print("程序正常运行")# 提示正常运行
