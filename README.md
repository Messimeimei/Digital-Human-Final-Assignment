# Digital-Human-Final-Assignment
代写的新传专业的数字人文期末作业，通过爬虫获取豆瓣电影排行榜所有类型电影前20名的影评，再对其进行简单的情感分析，并对结果进行可视化

文件结构介绍：

        1. spider.py    爬虫代码，用于爬取影评并保存到指定的本地文件夹
        
        2. movie_comment    即爬取下来的所有影评，一共是30个类别的电影，每个类别下有15部电影，每部电影200条影评
        
        3. utility      供主函数调用的其他工具代码，包括:
              -draw_imgs.py   绘制条形图等其他图形
              -langconv.py  辅助文字的预处理
              -make_wordcloud.py  绘制词云图
              -preprocess.py  用于文字的预处理，如去除特殊符号，停用词等等
              -zh_wiki.py   用于繁体字转化为简体字
        4. get_info.py      情感分析和绘制图形的主函数，调用分词包进行情感分析；调用绘图函数绘制词云图和条形图
        
        5. process_record_imgs    运行时的截图
        
        6. word_clouds      绘制的词云图和条形图
        
        7. img.png          词云图的背景图
        
        8. stopword_normal.txt    停用词表
