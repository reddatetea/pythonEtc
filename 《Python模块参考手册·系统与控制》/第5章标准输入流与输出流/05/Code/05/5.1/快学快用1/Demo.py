import sys
print('请输入姓名、性别、身高和体重（每一项用空格隔开）：') # 输出提示信息
for line in sys.stdin: # 使用sys.stdin读取标准输入流
    if line == '\n': # 如果用户什么都没有输入直接按下回车
        break # 终止for循环
    # 使用空格将用户输入的姓名、性别、身高和体重分隔开
    name, sex, height, weight = (x for x in line.split())
    print('姓名：' + str(name))
    print('性别：' + str(sex))
    print('身高（CM）：' + str(height))
    print('体重（KG）：' + str(weight))
    break # 终止for循环