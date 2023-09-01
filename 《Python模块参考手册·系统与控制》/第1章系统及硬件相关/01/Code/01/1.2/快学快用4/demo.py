import os
# 进入到目标文件夹
os.chdir("D:\\test\\")
# 创建名为“文本文档”的文件夹
os.system("mkdir 文本文档")
# 将目标文件夹中所有.txt后缀的文件都移动到“文本文档”的文件夹中
os.system("move *.txt ./文本文档/")
