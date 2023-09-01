from datetime import timedelta   # 导入 datetime 模块中的 timedelta 类

# 创建一个 timedelta 时间段对象
section = timedelta(weeks = 2, days = 2, hours = 8,\
                    minutes = 36, seconds = 46, milliseconds = 20 * 1000,\
                    microseconds = 10 * 1000 * 1000)
section_02 = timedelta(seconds = 10, milliseconds = 4 * 1000,
                       microseconds = 30 * 1000 * 1000)
format_str = "{:>24s} : {}"
print(format_str.format("第一个timedelta为", section))
print(format_str.format("第二个timedelta为", section_02))
# 加法
add = section + section_02
print(format_str.format("两 timedelta相加为", add))
# 减法
sub = section - section_02
print(format_str.format("两 timedelta相减为", sub))
# 乘法
mul = section_02 * 2
print(format_str.format("第二个 timedelta 乘以2为", mul))
# 除法
div = section_02 / 2
print(format_str.format("第二个 timedelta 除以2为", div))
# 两 timedelta 对象之间相除
delta_div = section / section_02
print(format_str.format("两个 timedelta 之间相除为", delta_div))
# 两 timedelta 对象之间地板除
floor_div = section // section_02
print(format_str.format("两个 timedelta 之间地板除为", floor_div))
# 正值取反
neg = -section_02
print(format_str.format("第二个 timedelta 的取反为", neg))
# 负值取反
com = -neg
print(format_str.format("负值 timedelta 的取反为", com))
# 绝对值运算
abs_num = abs(neg)
print(format_str.format("负值 timedelta 的绝对值为", abs_num))
# Hash 运算
has = hash(section_02)
print(format_str.format("第二个 timedelta 的 Hash 运算为", has))
