import os
old_file = "D:\\test\\demo.mp4"  # 原视频文件
cover_img = "D:\\test\\cover.jpg"  # 截取出的图片文件
# 第一个参数为ffmpeg.exe完整名，第二个参数为ffmpeg，后面接其他参数
os.execl("D:\\test\\ffmpeg.exe", "ffmpeg", "-i", old_file, "-f", "image2", "-r", "1", cover_img, "-y")
