# coding:   utf-8
# 作者(@Author):   榕城候佳人
# 创建时间(@Created_time): 2022/11/7 19:02
# 修改时间(@Modified_time): 2022/11/7 19:02


"""
    数据预处理部分，对影评进行停用词去除，特殊符号去除，并提供获得关键字功能
"""

import re
from utility import langconv
import jieba
import jieba.analyse
import jieba.posseg


class TextPreprocessor(object):

    def __init__(self, text=None, stopword_file=None):
        """
        stopword_file='data/stopwords/stopword_normal.txt'
        """
        self.text = text
        self.stopwords = self.init_stopwords(stopword_file)
        self.alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        self.number = [i for i in range(0, 10)]

    def traditional2simplified(self, text):
        '''将sentence中的繁体字转为简体字
            param: text
            return: 繁体字转换为简体字之后的文本
        '''
        if text == "":
            return text
        text = langconv.Converter('zh-hans').convert(text)
        return text

    def filter_trim(self, text):
        """特殊符号过滤
        """
        # 去除换行符
        reg = "[\r\n]+"
        text = re.sub(reg, "", text)
        # 去除特殊符号
        reg = "\\【.*】+|\\《.*》+|\\#.*#+|[./_$&%^*()<>+""'@|:~{}#]+|[0-9——\\=、：“”‘’￥……（）《》?【】\\[\\]a-z]+"
        text = re.sub(reg, '', text)
        reg = r"[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]"
        text = re.sub(reg, "", text)
        return text

    def init_stopwords(self, filepath):
        """初始化停留词
        """
        if filepath == None:
            return []
        stopwords = [line.strip() for line in open(filepath, encoding='UTF-8').readlines()]
        return stopwords

    def get_keyword(self, text):
        """获得关键词"""

        # 过滤句子的特殊字符
        text = self.filter_trim(text)

        result = jieba.analyse.extract_tags(text, topK=5)
        keywords = []
        for word in result:
            # 再进行一些简单的过滤
            if str(word)[0].startswith("一"):
                continue
            if str(word)[0] in self.number:
                continue
            if str(word) not in self.stopwords and str(word)[0] not in self.alpha:
                keywords.append(str(word))

        return keywords

    def get_name(self, text):
        """获得人名"""

        name = []
        seg = jieba.posseg.cut(text)
        for i in seg:
            if i.flag == 'nr' and i.word not in self.stopwords:
                name.append(i.word)
        return name

    def get_loc(self, text):
        """获得地名"""

        loction = []
        seg = jieba.posseg.cut(text)
        for i in seg:
            if i.flag == 'ns' and i.word not in self.stopwords:
                loction.append(i.word)
        return loction

    def get_time(self, text):
        """获得时间"""

        time = []
        seg = jieba.posseg.cut(text)
        for i in seg:
            if i.flag == 't' and i.word not in self.stopwords:
                time.append(i.word)
        return time

    def get_agency(self, text):
        """获得机构名"""

        agency = []
        seg = jieba.posseg.cut(text)
        for i in seg:
            if i.flag == 'nt' and i.word not in self.stopwords:
                agency.append(i.word)
        return agency

    def get_work(self, text):
        """获得作品"""

        works = []
        seg = jieba.posseg.cut(text)
        for i in seg:
            if i.flag == 'nw' and i.word not in self.stopwords:
                works.append(i.word)
        return works

    def get_normal_n(self, text):
        """获得普通名词"""

        time = []
        seg = jieba.posseg.cut(text)
        for i in seg:
            if i.flag == 'n' and i.word not in self.stopwords:
                time.append(i.word)
        return time

    def get_a(self, text):
        """获得形容词"""

        time = []
        seg = jieba.posseg.cut(text)
        for i in seg:
            if i.flag == "a" and i.word not in self.stopwords:
                time.append(i.word)
        return time

    def get_verb(self, text):
        """获得动词"""

        time = []
        seg = jieba.posseg.cut(text)
        for i in seg:
            if i.flag == 'v' and i.word not in self.stopwords:
                time.append(i.word)
        return time

    def get_other(self, text):
        """获得其他没用的词"""

        time = []
        seg = jieba.posseg.cut(text)
        for i in seg:
            if i.flag not in ['nr', 'ns', 't', 'nw', 'nt', 'n', 'a', 'v'] and i.word not in self.stopwords:
                time.append(i.word)
        return time


if __name__ == "__main__":
    preprocessor = TextPreprocessor(stopword_file='../stopword_normal.txt')
    text = """一哈，我不知那时候为什么看了这么多香港口水片……[]
    	"""
    text = preprocessor.get_name(text)
    print(text)
