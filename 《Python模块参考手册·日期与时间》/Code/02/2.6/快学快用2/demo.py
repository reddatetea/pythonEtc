import time

now = time.time()
now_ns = time.time_ns()
print('毫秒   ：', now)
print('纳秒   ：', now_ns)
ns = now_ns // 1000000  # 转换为毫秒
print('转换后  ：', ns)
