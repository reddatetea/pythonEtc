import sys     # 调用sys模块
sys.stdout.write('用户名称：')   # 正常输出，光标在最后一个字符后面
sys.stdout.write('张三丰')       # 在上一个光标处输出
sys.stdout.write('\n用户密码：')  # 先换行输出，光标在最后一个字符后面
sys.stdout.write('********\n')    # 在上一个光标处输出，输出完内容后换行到下一行行首
sys.stdout.write('确认密码：')
sys.stdout.write('********\n')    # 输出完内容后换行到下一行行首
sys.stdout.write('商品名称\t')    # 输出完内容后增加一个制表符距离
sys.stdout.write('商品价格\t')    # 输出完内容后增加一个制表符距离
sys.stdout.write('采购数量\t')    # 输出完内容后增加一个制表符距离
sys.stdout.write('商品金额')