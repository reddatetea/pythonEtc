import os
# 尝试读取python_home环境变量，如果python_home不存在，则返回第二个参数值
python_h = os.getenv("python_home", "C:\\Program Files\\Python")
print("Python解释器的路径为：" + python_h)
