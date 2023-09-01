import os

def checkJVM():  # 检查是否安装Java运行环境
    proxy = os.popen("java -version")  # 检查Java环境版本
    result = str(proxy.read())  # 读取命令结果
    if "不是内部或外部命令" in result:  # 如果命令无法执行
        return False
    else:
        return True

def run_java_code(java_code):  # 执行Java代码
    if checkJVM():  # 如果已安装Java运行环境
        with open("Demo.java", "w") as code_file:  # 在同级目录打开一个文件
            code_file.write(java_code)  # 写入Java代码
        os.system("javac Demo.java")  # 编译Java代码
        proxy = os.popen("java Demo")  # 执行Java代码
        result = proxy.read()  # 读取执行结果
        print(result)
    else:
        print("未安装JER环境，无法执行Java程序")

java_code = """
public class Demo {
   public static void main(String[] args) {
      System.out.println("Hello Python, this is Java !");
   }
}
"""

run_java_code(java_code)  # 运行Java代码
