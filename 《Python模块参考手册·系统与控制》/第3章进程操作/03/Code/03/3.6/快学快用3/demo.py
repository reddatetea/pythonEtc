import os  # 文件与操作系统相关模块
print("进程号是：",os.getpid())
i=int(input("请输入想要杀死进程的指定退出代码："))
os.kill(os.getpid(),i)  # 杀死当前进程
print("此处有毒，已杀死")
