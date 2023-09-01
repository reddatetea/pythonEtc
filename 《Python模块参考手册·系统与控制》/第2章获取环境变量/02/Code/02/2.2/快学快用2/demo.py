import os                                             # 文件与操作系统相关模块
newvar = 'JAVA_HOME'                                 # 环境变量名称
try:
    print(newvar+'已经存在！值为：')
    print(os.environ[newvar])                         # 输出环境变量的值
except:
    os.environ[newvar] = r'C:\Java\jdk1.8.0_181'     # 创建环境变量
    print(os.environ[newvar])                          # 输出环境变量的值
