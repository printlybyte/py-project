import matplotlib.pyplot as plt
class utfinit:
    def __init__(self):
        # 支持中文 plt
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
