# ch7_15_1.py
fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
print("目前fruits串列 : ", fruits)

for fruit in fruits[:]:
    fruits.remove(fruit)
    print("刪除 %s " % fruit)
    print("目前fruits串列 : ", fruits)







