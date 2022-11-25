# coding:   utf-8
# 作者(@Author):   榕城候佳人
# 创建时间(@Created_time): 2022/11/20 14:51
# 修改时间(@Modified_time): 2022/11/20 14:51

"""制作词云图"""
import os

from matplotlib import colors
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image


def wordcloud_(text, file_path, file_name, img_path='E:\PycharmProjects\Web项目\综合项目\img.png'):
    """
    制作词云图
    :param text: 文本
    :param img_path: 背景图片的路径
    :param file_name:词云图名称
    :param file_path:词云图所在文件夹
    :return: None
    """

    # 设置背景图片
    backgroud = np.array(Image.open(img_path))

    # 自定义颜色列表
    color_list = ['#CD853F', '#DC143C', '#00FF7F', '#FF6347', '#8B008B', '#00FFFF', '#0000FF', '#8B0000', '#FF8C00',
                  '#1E90FF', '#00FF00', '#FFD700', '#008080', '#008B8B', '#8A2BE2', '#228B22', '#FA8072', '#808080']

    colormap = colors.ListedColormap(color_list)

    # 制作词云图
    wc = WordCloud(width=2000, height=1400,
                   background_color='white',
                   mask=backgroud,  # 添加蒙版，生成指定形状的词云，并且词云图的颜色可从蒙版里提取
                   max_words=1000,
                   stopwords=open('./stopword_normal.txt', encoding='utf-8').read().split('\n'),  # 内置的屏蔽词,并添加自己设置的词语
                   font_path='C:\Windows\Fonts\simhei.ttf',
                   relative_scaling=0.5,  # 设置字体大小与词频的关联程度为0.4
                   random_state=50,
                   scale=8,
                   colormap=colormap,
                   ).generate(text)


    # 保存词云图
    path = os.path.join("E:\PycharmProjects\Web项目\综合项目\word_clouds", file_path)
    path = path.strip()
    path = path.rstrip("\\")
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)

    wc.to_file(os.path.join('./word_clouds', path, file_name),)
