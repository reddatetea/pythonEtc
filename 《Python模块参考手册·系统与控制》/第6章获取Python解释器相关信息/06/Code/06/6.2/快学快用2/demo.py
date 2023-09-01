import sys
# 从获取的版本信息中截取主版本号、次版本号和生成号的组合，并判断
if sys.version[0:5] == '3.8.2':
    print('您当前使用的是Python 3.8.2版本')
else:
    sys.exit() # 退出程序