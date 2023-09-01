import datetime

nol = -52  # 使用负数天数
bm = datetime.date.max.toordinal()  # 获取最大天数
print(f"最大天数为：{bm}")
try:
    bgl = datetime.date.fromordinal(nol)  # 转换为日期
    print("公历1日前的某个日期:%s" % bgl)  # 不会执行
except ValueError as Ex:
    print("使用负数天数报错: ", Ex)

try:
    am = datetime.date.fromordinal(bm + 1)  # 超出最大天数
    print("公历的日期超出 %d:%s" % (bm, am))  # 不会执行
except ValueError as Ex:
    print(f"超出最大天数报错：", Ex)
