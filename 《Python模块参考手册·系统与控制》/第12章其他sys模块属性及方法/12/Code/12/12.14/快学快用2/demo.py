import sys
def div(): # 定义除法函数，使除数为0
    return 1 / 0
def first(): # 第一层堆栈信息
    div()
def second(): # 第二层堆栈信息
    first()
def myExcepthook(types, value, traceback):  # 自定义异常
    print("异常类型：{}".format(types))
    print("异常对象：{}".format(value))
    i = 1
    while traceback:
        print("第{}层堆栈信息".format(i))
        tracebackCode = traceback.tb_frame.f_code # 获取异常详细信息
        print("文件名：{}".format(tracebackCode.co_filename)) # 输出文件名
        print("函数或者模块名：{}".format(tracebackCode.co_name)) # 输出函数或模块名
        traceback = traceback.tb_next
        i += 1
sys.excepthook = myExcepthook # 指定自定义异常
second() # 调用会发生异常的函数
sys.excepthook=sys.__excepthook__ # 重置异常