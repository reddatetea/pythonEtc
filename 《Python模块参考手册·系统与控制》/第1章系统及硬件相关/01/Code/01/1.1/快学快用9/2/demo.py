import os

def checkJVM():
    proxy = os.popen("java -version")  # 检查Java环境版本
    result = str(proxy.read())  # 读取命令结果
    if "不是内部或外部命令" in result:  # 如果命令无法执行
        return False
    else:
        return True

if checkJVM():
    os.chdir("D:\\test")  # 进入Java文件所在的文件夹
    os.system("javac Demo.java")  # 编译Java源码文件
    proxy = os.popen("java Demo")  # 执行Java字节码
    result = proxy.read()  # 读取执行结果
    print(result)  # 打印Java代码的执行结果
else:
    print("未安装JER环境，无法执行Java程序")
