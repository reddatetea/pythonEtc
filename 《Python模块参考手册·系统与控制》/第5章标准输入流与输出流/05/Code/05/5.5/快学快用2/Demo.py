import sys
import time
sys.stdout.write('程序正在安装，请稍后')
sys.stdout.write("\n")
for i in range(20):
    sys.stdout.write('#')
    time.sleep(0.3)