import os
old_file = "D:\\test\\demo.mp4"  # 原始视频文件
new_file = "D:\\test\\demo.avi"  # 转换之后的文件
# 参数写在列表里
avg = ["ffmpeg", "-i", old_file, "-vcodec", "copy", "-acodec", "copy", new_file, "-y"]
# 第一个参数为ffmpeg.exe完整名，第二个参数为其他参数列表
os.execv("D:\\test\\ffmpeg.exe", avg)
