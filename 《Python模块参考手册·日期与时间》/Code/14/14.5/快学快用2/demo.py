from calendar import Calendar     # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
itermonth= calendar_obj.itermonthdays3(2020,8)  # 获取2020年8月份内的（年、月、日）
for i in itermonth:               # 循环遍历迭代器中的（年、月、日）
    # 仅输出月份为8且日小于5的日期，并格式化
    if i[1]==8 and i[2]<5:
        print ('原格式：',i,"格式化后： %s年%s月%s日" % (i[0], i[1], i[2]))
