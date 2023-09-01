import sys
print('请输入姓名、性别、身高和体重（每一项用空格隔开）：') # 输出提示信息
name, sex, height, weight = sys.stdin.readline().split() # 多数据输入
print('姓名：' + str(name))
print('性别：' + str(sex))
print('身高（CM）：' + str(height))
print('体重（KG）：' + str(weight))