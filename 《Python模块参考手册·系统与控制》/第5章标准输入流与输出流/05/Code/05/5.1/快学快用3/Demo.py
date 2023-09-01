import sys
print('输入两个点坐标：') # 输出提示信息
for line in sys.stdin: # 使用sys.stdin读取标准输入流
    if line == '\n': # 如果用户什么都没有输入直接按下回车
        break # 终止for循环
    x1, y1, x2, y2 = (float(x) for x in line.split()) # 使用空格将两个点的横、纵坐标分隔开
    k = (y2 - y1) / (x2 - x1) # 根据这两个点的横、纵坐标计算连接这两个点的直线的斜率
    print('斜率：' + str(k)) # 输出计算后的斜率
    break # 终止for循环