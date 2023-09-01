import sys
print('请输入a, b, e, c, d, f的值：') # 输出提示信息
for line in sys.stdin: # 使用sys.stdin读取标准输入流
    if line == '\n': # 如果用户什么都没有输入直接按下回车
        break # 终止for循环
    # 使用空格将用户输入的a, b, e, c, d, f的值分隔开
    a, b, e, c, d, f = (float(x) for x in line.split())
    x = (e * d - b * f) / (a * d - b * c) # 计算x的值
    y = (a * f - e * c) / (a * d - b * c) # 计算y的值
    print('x =', x, '，y =', y)
    break # 终止for循环