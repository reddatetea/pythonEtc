import sys     # 调用sys模块
import time
sys.stderr.write('打开程序时遇到错误，请稍后\n')
for i in range(20):
    sys.stderr.write("\r")
    if i%2==1 :
        sys.stderr.write("\\")
    else:
        sys.stderr.write("/")
    time.sleep(0.3)