import sys
# 定义一个函数，用来作为探查器函数，必须定义3个参数
def Test(frame,event,arg):
    caller=frame.f_back # 获取当前堆栈
    print('call',caller) # 返回调用的堆栈信息
def testA(): # 测试输出
    print('testA')
def testB(): # 测试输出
    print('testB')
    testA() # 调用testA()
print('默认探查器函数：', sys.getprofile())  # 获取默认探查器函数
sys.setprofile(Test) # 设置探查器函数
testB() # 调用testB()
print('设置的探查器函数：',sys.getprofile()) # 获取设置的探查器函数