import os

proxy = os.popen('systeminfo')  # 执行命令，返回通道的代理文件流
result = proxy.read()  # 读取文件流中的内容
for line in result.splitlines():  # 将内容按行拆分
    line = str(line).strip()  # 行内容转为字符串，去掉首尾空白
    if "物理内存总量" in line:  # 如果包含"物理内存总量" 字样
        print(line)  # 打印内存总量
        datas = line.split()  # 按照空白内存分割
        total_memory = datas[1].replace(",", "")  # 去掉第二个元素中的逗号，作为内存总量
    elif "可用的物理内存" in line:  # 如果包含"可用的物理内存" 字样
        print(line)  # 打印可用内存
        datas = line.split()  # 按照空白内存分割
        available_memory = datas[1].replace(",", "")  # 去掉第二个元素中的逗号，作为已用内存
        break

available_memory = float(available_memory)  # 字符串转为浮点型
total_memory = float(total_memory)
used_memory = total_memory - available_memory  # 已用内存
percentage = used_memory / total_memory  # 内存利用率
print("内存使用率：" + str(int(percentage * 100)) + "%")
