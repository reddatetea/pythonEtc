from time import perf_counter

def func():
    print('func is running')

t0 = t1 = perf_counter()
delta = 1  # 每秒执行一次函数
while True:
    while t1 - t0 > delta:
        t0 = perf_counter()
        func()
    t1 = perf_counter()
