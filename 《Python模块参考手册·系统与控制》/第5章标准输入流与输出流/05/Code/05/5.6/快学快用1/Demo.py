import sys     # 调用sys模块
import time
sys.stdout.write('动态输出跑马灯文字\n')
for i in range(20):
    for j in range(6):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.3)