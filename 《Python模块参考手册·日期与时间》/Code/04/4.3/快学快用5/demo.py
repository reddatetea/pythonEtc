import random  # 导入随机模块
import time  # 导入时间模块
import requests  # 网络请求模块
from bs4 import BeautifulSoup  # html解析模块

url = 'http://quotes.toscrape.com/page/{number}/'  # 请求地址
# 创建请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
for page in range(1, 4):  # 循环执行3次
    response = requests.get(url.format(number=page), headers=headers)  # 发送网络请求
    if response.status_code == 200:  # 请求成功
        # 创建一个BeautifulSoup对象，获取页面正文
        soup = BeautifulSoup(response.text, features="lxml")
        all = soup.find_all('div', class_='quote')  # 获取所有内容
        author_list = []  # 保存作者的列表
        for i in all:  # 遍历每个信息
            author = i.find('small', class_='author').text  # 获取作者名称
            author_list.append(author)  # 将作者信息添加至列表
        print('第',page,'页名句作者如下：')
        print(author_list)
    if page<3:    # 判断网页的页数小于3
        random_time = random.randint(1, 4)  # 创建随机时间
        print('休息', random_time, '秒再次爬取下一页数据！')
        time.sleep(random_time)  # 等待随机时间
