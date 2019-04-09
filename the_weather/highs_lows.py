import csv
from matplotlib import pyplot as plt
from datetime import datetime as da

filename = 'sitka_weather_07-2014.csv'


def plt_show(dates,highs):
    # 根据数据绘制图形
    # fig = plt.figure(dpi=128, figsize=(10, 6))
    fig =plt.figure(figsize=(10, 6))
    plt.plot(dates,highs, c='red')
    # 设置图形的格式
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    hights ,dates= [],[]
    for row in reader:
        hights.append(int(row[1]))
        dates.append(da.strptime(row[0],"%Y-%m-%d"))
    print(dates)
    plt_show(dates,hights)


