import time
from datetime import date  # 导入datetime模块中的 date 类

struct01 = time.localtime()
struct02 = date.today().timetuple()    # 获取当前日期对象，并提取结构化时间
print(f"struct02 = {struct02}")
if type(struct01) == type(struct02):
    print("类型相等")
print(f"类型为： {type(struct02)}")
# 按照 time 模块的时间固定字符串格式输出
print("struct01 time.astime = ", time.asctime(struct01))
print("struct02 time.astime = ", time.asctime(struct02))
