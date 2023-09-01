import requests                      # 导入网络请求模块
from fake_useragent import UserAgent # 导入请求头模块
from multiprocessing import Pool     # 导入进程池
import re                            # 导入正则表达式
import time                          # 导入时间模块
class Spider():
    def __init__(self):
        self.info_urls = []         # 所有电影详情页的请求地址

    # 获取首页信息
    def get_home(self, home_url):
        header = UserAgent().random  # 创建随机请求头
        home_response = requests.get(home_url, header)  # 发送首页网络请求
        if home_response.status_code == 200:  # 判断请求是否成功
            home_response.encoding = 'gb2312'  # 设置编码方式
            html = home_response.text  # 获取返回的html代码
            # 获取所有电影详情页地址
            details_urls = re.findall('<a href="(.*?)" class="ulink">', html)
            self.info_urls.extend(details_urls)  # 添加请求地址列表
if __name__ == '__main__':       # 创建程序入口
    # 创建主页请求地址的列表
    home_url = ['https://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
                    .format(str(i))for i in range(1,11)]
    s = Spider()   # 创建自定义爬虫类对象
    start_time = time.time()              # 记录串行爬取电影详情页地址的起始时间
    for i in home_url:                    # 循环遍历主页请求地址
        s.get_home(i)               # 发送网络请求，获取每个电影详情页地址
    end_time = time.time()                 # 记录串行爬取电影详情页地址结束时间
    print('串行爬取电影详情页地址耗时：',end_time-start_time)

    start_time_4 = time.time()             # 记录四进程爬取电影详情页地址起始时间
    pool = Pool(processes=4)               # 创建4进程对象
    pool.map(s.get_home,home_url)          # 通过进程获取每个电影详情页地址
    end_time_4 = time.time()               # 记录四进程爬取电影详情页地址结束时间
    print('4进程爬取电影详情页地址耗时:', end_time_4 - start_time_4)
