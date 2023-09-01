import os
import sys
try:
    import jieba # 导入jieba分词模块
except:
    print(sys.exc_info())  # 捕获并输出异常相关信息
    os.system('pip install jieba') # 安装jieba