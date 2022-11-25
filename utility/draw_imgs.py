# coding:   utf-8
# 作者(@Author):   榕城候佳人
# 创建时间(@Created_time): 2022/11/20 19:16
# 修改时间(@Modified_time): 2022/11/20 19:16

"""用于数据可视化，即绘制各种图形"""

import matplotlib.pyplot as plt


def draw_pie(info, title="ss", path=None):
    """
    绘制饼状图
    :param title: 图片标题
    :param info: 列表形式的信息
    :param path: 保存路径
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    x = [info[i][0] for i in range(len(info))]
    y = [info[i][1] for i in range(len(info))]


    # 创建颜色序列
    colors = []
    for _ in range(int(len(info) / 2)):
        colors.append([_ / int(len(info) / 2), 0.5, 0.5])
    colors = colors + colors[::-1]

    plt.tick_params(axis='x', labelsize=8)  # 设置x轴标签大小

    # 绘制条形图
    plt.bar(x, y, color=colors, width=0.5)
    for x, z in zip(range(len(y)), y):
        plt.text(x - 0.3, z, z)

    plt.title(title)
    plt.savefig(path, dpi=300)

    # 记得关闭图像，不然就寄咯
    plt.close()


if __name__ == '__main__':
    a = [('不错', 105), ('孤独', 105), ('自由', 105), ('美好', 81), ('幸福', 79), ('简单', 70), ('完美', 67), ('平淡', 65),
         ('残酷', 60), ('成功', 59), ('充满', 57), ('潦倒', 55), ('冷静', 53), ('年轻', 52), ('很棒', 50), ('优秀', 44),
         ('勇敢', 40), ('温柔', 38), ('遗憾', 37), ('尊重', 36)]
    b= [('美好', 133), ('不错', 108), ('简单', 103), ('善良', 96), ('充满', 64), ('纯真', 62), ('有趣', 60), ('快乐', 51),
        ('清新', 46), ('欢乐', 42), ('真挚', 41), ('细腻', 41), ('完美', 39), ('邋遢', 38), ('幸福', 36), ('幽默', 32),
        ('很棒', 30), ('温柔', 28), ('惊艳', 26), ('成功', 25)]
    c= [('美好', 203), ('完美', 152), ('特效', 94), ('简单', 88), ('不错', 83), ('善良', 83), ('宏大', 62), ('充满', 62),
        ('勇敢', 61), ('纯真', 57), ('邪恶', 48), ('遗憾', 47), ('幸福', 47), ('年轻', 45), ('孤独', 45), ('成功', 44),
        ('有趣', 42), ('最爱', 40), ('快乐', 40), ('幽默', 36)]
    d = [a, b, c]
    for i in range(3):
        draw_pie(info=d[i],path = f'E:\PycharmProjects\Web项目\综合项目\{i}.jpg')
