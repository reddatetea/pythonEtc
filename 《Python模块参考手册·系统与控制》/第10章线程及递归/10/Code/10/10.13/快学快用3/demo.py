import sys
list=sys.get_asyncgen_hooks() # 使用列表存储asyncgen_hooks对象
d=eval('{'+'\'firstiter\':{0},\'finalizer\':{1}'.format(list[0],list[1])+'}') # 转换为字典
for key,value in d.items(): # 遍历字典
    print(key,":",value) # 输出键值