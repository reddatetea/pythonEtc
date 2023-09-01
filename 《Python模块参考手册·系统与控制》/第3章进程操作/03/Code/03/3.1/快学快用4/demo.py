import os  # 文件与操作系统相关模块
times = os.times()  # 返回当前的全局进程时间
if times.elapsed==0:
    # 返回自过去的固定点以来经过的实时时间
    print('Windows系统的自过去的固定点以来经过的实时时间是:',times.elapsed) 
else:
    print('windows系统存在值')
