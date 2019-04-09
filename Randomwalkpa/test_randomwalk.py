import matplotlib.pyplot as plt
from Randomwalkpa.random_walk import RandomWalk
from Randomwalkpa.pltutf import utfinit

def plt_show():
    # 指定大小
    # plt.figure(figsize=(6, 6.5))
    plt.xlabel("x")


    plt.ylabel("y")
    plt.title("随机漫步")
    # 消除圆点背景 指定渐变颜色值
    plt.scatter(ra.x_values, ra.y_values, c=ra.x_values, cmap=plt.cm.Blues, edgecolor='none', s=5)
    # 突出起点和终点
    plt.scatter( 0,0,c="green",edgecolor='none',s=100)
    plt.scatter(ra.x_values[-1], ra.y_values[-1], c='red', edgecolors='none',s=100)
    # 消除圆点背景 指定红色
    # plt.scatter(ra.x_values,ra.y_values,c="red",edgecolor='none',s=5)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()


if __name__ == '__main__':
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    ut = utfinit()
    # 只要程序处于活动状态，就不断地模拟随机漫步
    while True:
        ra = RandomWalk()
        ra.fill_walk()
        plt_show()
        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n':
            break