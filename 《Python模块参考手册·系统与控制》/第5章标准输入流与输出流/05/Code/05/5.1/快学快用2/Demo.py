import sys
print('请输入用户名和密码：') # 输出提示信息
for line in sys.stdin: # 使用sys.stdin读取标准输入流
    if line == '\n': # 如果用户什么都没有输入直接按下回车
        break # 终止for循环
    # 使用空格将用户输入的用户名和密码分隔开
    username, password = (x for x in line.split())
    # 验证用户输入的用户名和密码是不是mrsoft和123456
    if username == 'mrsoft' and password == '123456':
        print('正在进入主页面……')
        break # 终止for循环
    else:
        print('用户名或密码错误，请重新输入！')
        print('请输入用户名和密码：')
        continue # 跳过本次for循环