import csv
from matplotlib import pyplot as plt
from datetime import datetime as da
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
filename = 'sitka_weather_2014.csv'

def plt_show(dates,highs,lows):
    # 根据数据绘制图形
    # fig = plt.figure(dpi=128, figsize=(10, 6))
    fig =plt.figure(figsize=(10, 6))
    plt.plot(dates,highs, c='red',alpha=0.5 )
    plt.plot(dates,lows, c='blue',alpha=0.5 )
    # 设置着色器
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # 设置图形的格式
    # plt.title("Daily high temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 从文件中获取日期、最高气温和最低气温
    hights ,dates,lows= [],[],[]
    for row in reader:
        try:
            current_date=da.strptime(row[0],"%Y-%m-%d")
        except ValueError:
            print("errmsg"+str(current_date))
        else:
            dates.append(current_date)
            hights.append(int(row[1]))
            lows.append(int(row[3]))
    plt_show(dates,hights,lows)
    print(lows)



