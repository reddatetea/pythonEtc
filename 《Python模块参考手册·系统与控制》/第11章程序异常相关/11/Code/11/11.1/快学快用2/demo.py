import sys
import pymysql
try:
    db = pymysql.connect("localhost", "root", "root", "db") # 连接数据库
except:
    print(sys.exc_info())  # 捕获并输出异常相关信息