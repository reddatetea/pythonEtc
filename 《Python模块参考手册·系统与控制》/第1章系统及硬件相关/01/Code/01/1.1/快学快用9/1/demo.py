import os

def checkJVM():
    proxy = os.popen("java -version")  # 检查Java环境版本
    result = str(proxy.read())  # 读取命令结果
    if "不是内部或外部命令" in result:  # 如果命令无法执行
        return False
    else:
        return True

if checkJVM():
    print("可以执行Java程序")
else:
    print("未安装JER环境，无法执行Java程序")
