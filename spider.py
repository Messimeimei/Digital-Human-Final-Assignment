# coding:   utf-8
# 作者(@Author):   榕城候佳人
# 创建时间(@Created_time): 2022/11/7 19:02
# 修改时间(@Modified_time): 2022/11/17 17:30

"""
    爬取豆瓣电影评论
"""

import requests
from bs4 import BeautifulSoup
import os
import time

# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',

}

# 主网页
url = 'https://movie.douban.com/chart'

# 设置代理,
proxies = {
    # 'http': '172.30.6.14:8880',
    # 'http': "36.152.44.96:5000",          # 百度ip
    # "http": '111.30.144.71:5000',         # QQip
    # 'http': '47.103.24.173:5000',         # b站ip
    # 'http': ' 192.168.210.53:5000',       # 本地ip
    # 'http': '60.205.172.2:5000',          # CSDNip
    'http': "49.233.242.15:5000",  # 豆瓣ip（doge，想不到吧）
    # 'http': '120.233.21.30:5000',         # 微信ip
    # 'http': '103.41.167.234:5000',        # 知乎ip
    # 'http': '39.156.68.154:5000',         # hao123ip
    # 'http': '36.152.218.86:5000',         # 凤凰网ip
    # 'http': '151.101.78.137:5000',        # 人民网ip
    # 'http': '221.178.37.218:5000',        # 中国网ip

}

# 解决乱码问题
response = requests.get(url, headers=headers, proxies=proxies)
response.encoding = 'utf-8'

# 获得不同类型电影的url
response = response.text
main_soup = BeautifulSoup(response, 'html.parser')
dif_movies = main_soup.select('#content > div > div.aside > div:nth-child(1) > div')
movie_types = []  # 存储不同类型电影的页面url
urls = dif_movies[0].find_all('a')

# 获得不同类型电影的代号和名称
for url in urls:
    param = url['href']
    index1 = param.find("&type=")
    index2 = param.find("&interval_id=")
    type_num = param[index1 + 6:index2]  # 电影类型代号
    type_name = param[20:index1]  # 电影类型名称
    movie_types.append((type_num, type_name))

# 爬取不同类型电影中前15的电影评论
for type, movie_class in movie_types:
    print(f"{'*' * 20}开始爬取->{movie_class}<-类型的电影{'*' * 20}")

    movie_url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        "start": "0",
        "limit": "20",
        "type": f"{type}",
        "interval_id": "100:90",
        "action": "",

    }
    response = requests.get(movie_url, headers=headers, params=param, proxies=proxies)
    time.sleep(1)  # 限制请求时间，防止被封ip
    response.encoding = 'utf-8'
    movie_data = response.json()

    # 存放这个类型下前二十的电影的网址和名称
    urls = []
    for data in movie_data:
        urls.append((data['url'], data['title']))

    # 创键对应的电影类型目录
    path = os.path.join("E:\PycharmProjects\Web项目\新传数字人文项目", movie_class)
    path = path.strip()
    path = path.rstrip("\\")

    if os.path.exists(path):
        print(f"已经爬取该页面{movie_class}")
        continue
    else:
        os.makedirs(path)

    # 爬取每一部电影前10页的电影评论，共计200条
    for url in urls:
        if os.path.exists(os.path.join(path, f"{url[1]}_200条影评.txt")):
            print(f'《{url[1]}》已经爬取')
            continue

        # 获得这部电影下前十页的影评网址
        comment_urls = []
        head_url = url[0] + 'comments?limit=20&status=P&sort=new_score'  # 影评网址首页
        comment_urls.append(head_url)
        for i in range(20, 201, 20):
            other_url = url[0] + f"comments?start={i}&limit=20&status=P&sort=new_score"
            comment_urls.append(other_url)  # 后续9个影评网页

        # 爬取所有的200个影评并保存到对应文件
        print(f"===开始爬取电影《{url[1]}》的200条影评===")
        for comment_url in comment_urls:
            response = requests.get(comment_url, headers=headers, proxies=proxies)
            time.sleep(1)  # 限制次数，防止被封ip
            response.encoding = 'utf-8'
            response = response.text

            # 定位到评论所在的地方
            soup = BeautifulSoup(response, 'html.parser')
            comments = soup.select("#comments")
            try:
                comments_ = comments[0].find_all("span", class_='short')
            except IndexError:
                continue

            # 存放最终一条条评论
            final_comments = []
            for comment in comments_:
                final_comments.append(comment.text.strip())

            # 写入文件夹
            with open(os.path.join(path, f"{url[1]}_200条影评.txt"), 'a', encoding='utf-8') as f:
                for comment in final_comments:
                    f.write(comment + '\n')
        print(f"===电影《{url[1]}》的200条影评爬取完毕===")
        time.sleep(5)
