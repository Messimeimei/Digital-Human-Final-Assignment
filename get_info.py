# coding:   utf-8
# 作者(@Author):   榕城候佳人
# 创建时间(@Created_time): 2022/11/19 9:03
# 修改时间(@Modified_time): 2022/11/19 9:03

"""
    对电影评论提取关键词
"""

import os

import jieba

from utility.draw_imgs import draw_pie
from utility.make_wordcloud import wordcloud_
from utility.preprocess import TextPreprocessor

# 文本处理器
processor = TextPreprocessor(stopword_file="stopword_normal.txt")


def emotion_analyse(info: list):
    """
    情感分析,统计所有出现的情感词个数，取前20个做条形图
    :param:info:一个类型的电影的所有情感词
    :return:该类型电影下，字典形式的出现次数前二十的情感词
    """

    dict_word = {}
    for i in range(len(info)):
        # 情感词长度大于2
        if len(info[i]) == 1:
            continue
        if info[i] not in dict_word:
            dict_word[info[i]] = 1
        else:
            dict_word[info[i]] += 1
    word_sorted = sorted(dict_word.items(), key=lambda x: x[1], reverse=True)

    return word_sorted[:20]


if __name__ == '__main__':

    # 打开不同类型电影影评所在文件夹
    classes = os.listdir('movie_comment')

    for movie_class in classes:
        # 获得该类型电影下的所有电影影评所在文件
        movies = os.listdir('movie_comment/' + movie_class)

        # 存储整个类型下的不同影评信息
        whole_name = []
        whole_loc = []
        whole_time = []
        whole_agency = []
        whole_works = []
        whole_n = []
        whole_a = []
        whole_v = []
        whole_other = []

        # 获得单个电影的影评信息
        for movie in movies:
            with open(os.path.join('movie_comment/', movie_class, movie), 'r', encoding='utf-8') as f:
                # 所有的影评句子
                sentences = f.read()

                # 保留所有单个电影的信息，方便后面整个类型的统计
                whole_a.extend(processor.get_a(sentences))
                # whole_name.extend(processor.get_name(sentences))
                # whole_loc.extend(processor.get_loc(sentences))
                # whole_time.extend(processor.get_time(sentences))
                # whole_name.extend(processor.get_time(sentences))
                # whole_agency.extend(processor.get_agency(sentences))
                # whole_works.extend(processor.get_work(sentences))
                # whole_n.extend(processor.get_normal_n(sentences))
                # whole_v.extend(processor.get_verb(sentences))

                # 保存情感倾向词云图
                wordcloud_(text=' '.join(processor.get_a(sentences)), file_path=movie_class,
                                file_name=movie[:-11] + '_情感词云图.jpg')

        # 绘制该类型电影情感词的条形统计图
        emotion_words = emotion_analyse(whole_a)
        path = os.path.join('./word_clouds', movie_class, movie_class + '_情感词语条形统计图.jpg')
        draw_pie(title=f"{movie_class}情感分析图", info=emotion_words, path=path)

        # 绘制该类型电影的情感词云图
        wordcloud_(text=' '.join(whole_a), file_path=movie_class, file_name=movie_class + "_情感词云图.jpg")
        print(f"完成{movie_class}部分")
