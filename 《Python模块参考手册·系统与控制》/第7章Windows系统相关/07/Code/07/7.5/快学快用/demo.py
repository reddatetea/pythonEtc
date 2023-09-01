import sys
# 定义一个函数，用来作为跟踪函数，必须定义3个参数
def Test(frame,event,arg):
    caller=frame.f_back # 获取当前堆栈
    print('call',caller) # 返回调用的堆栈信息
def testA(): # 测试输出
    print('testA')
def testB(): # 测试输出
    print('testB')
    testA() # 调用testA()
print('默认跟踪函数：', sys.gettrace())  # 获取默认跟踪函数
sys.settrace(Test) # 设置跟踪函数
testB() # 调用testB()
print('设置的跟踪函数：',sys.gettrace()) # 获取设置的跟踪函数