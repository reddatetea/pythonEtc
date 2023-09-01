import time  # 导入time模块
tz=time.tzname      # 获取计算机当前标准时区与夏令时时区名称
print('返回的元组信息为：',tz)
# 由于返回的元组信息为乱码，所以需要进行编码后输出
print('标准时区名称为：',tz[0].encode('latin-1').decode('gbk'))
print('夏令时时区名称为：',tz[1].encode('latin-1').decode('gbk'))
