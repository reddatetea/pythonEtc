import os  # 文件与操作系统相关模块  
if os.getpid()<100 and os.getpid()>0:# 进程ID在0~100之间
    print("当前进程号是:",os.getpid(),"我是A进程，Follw me,加油干!!!")
elif os.getpid() < 1000 and os.getpid() > 100:# 进程ID在100~1000之间
    print("当前进程号是:", os.getpid(), "我是B进程，加油，今天又是元气满满~~")
elif os.getpid() < 10000 and os.getpid() > 1000:# 进程ID在1000~10000之间
    print("当前进程号是:", os.getpid(), "我是C进程，伙计们，起床干活啦--")
else:
    print("当前进程号是:", os.getpid(),"我太累了，休息一会")
