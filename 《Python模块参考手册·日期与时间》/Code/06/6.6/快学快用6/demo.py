import datetime

tt = (11, 59, 59, 9999)  # 定义一个时间元组
ti = datetime.time(*tt)  # 使用splat运算符解压缩时间元素并创建时间实例，注意添加*
print('ti：', ti, '，类型为：', type(ti))
