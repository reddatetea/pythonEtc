import os  # 文件与操作系统相关模块
os.kill(os.getppid(),2)  # 杀死父进程
