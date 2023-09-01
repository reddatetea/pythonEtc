import os
proxy = os.popen("wmic cpu get name")  # 执行命令，返回通道的代理文件流
result = proxy.read()  # 读取文件流中的内容

if len(result) > 0:  # 如果返回有内容的结果
    for line in result.splitlines():  # 将内容按行拆分
        line = str(line)  # 行内容转为字符串
        if "GHz" in line:
            # 用@分割出cpu的频率字符串
            hz_str = line.split("@")[1].strip()
            hz = hz_str[0:-3]  # 删除字符串结尾的“GHz”三个字符
            hz = float(hz)  # 字符串转为浮点数
            if hz > 2.2:  # 如果大于最低性能
                print("程序支持本计算机CPU。（频率：" + hz_str + "）")
            else:
                print("CPU频率过低，无法运行程序。（频率为" + hz_str + "）")
else:
    print("系统不兼容命令")
