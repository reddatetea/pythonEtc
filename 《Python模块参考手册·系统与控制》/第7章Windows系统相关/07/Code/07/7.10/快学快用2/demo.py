import sys
import os
path = os.getcwd()#获取当前目录
try:
    finder = sys.path_importer_cache[path]#获取指定路径的查找程序
except KeyError:
    finder = sys.path_hooks#创建finder
    sys.path_importer_cache[path] = finder#定义查找程序缓存
print(sys.path_importer_cache[path])