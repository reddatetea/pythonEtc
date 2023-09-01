import sys     # 调用sys模块
import time
sys.stdout.write('杀毒程序正在全盘检查，请稍后\n')
for i in range(20):
    sys.stdout.write("\r")
    if i%2==1 :
        sys.stdout.write("\\")
    else:
        sys.stdout.write("/")
    sys.stdout.flush()
    time.sleep(0.3)