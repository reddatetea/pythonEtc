import os
proxy = os.popen("dir /b D:\\test")  # 执行命令，返回通道的代理文件流
result = proxy.read()  # 读取文件流中的内容
for line in result.splitlines():  # 将内容按行拆分
    print(str(line).strip())  # 输出每一行的文本内容
