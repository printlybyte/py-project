# coding: utf-8

import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print()


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for t in ilt:
        count = count + 1
        print(tplt.format(count, t[0], t[1]))


def main():
    goods = '高达'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()

def get_html(url):
    """获取源码html"""
    try:
        r = requests.get(url=url, timeout=10)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("获取失败")


def get_data(html, goodlist):
    """使用re库解析商品名称和价格
    tlist:商品名称列表
    plist:商品价格列表"""
    tlist = re.findall(r'\"raw_title\"\:\".*?\"', html)
    plist = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
    for i in range(len(tlist)):
        title = eval(tlist[i].split(':')[1])  # eval()函数简单说就是用于去掉字符串的引号
        price = eval(plist[i].split(':')[1])
        goodlist.append([title, price])


def write_data(list, num):
    # with open('E:/Crawler/case/taob2.txt', 'a') as data:
    #    print(list, file=data)
    for i in range(num):  # num控制把爬取到的商品写进多少到文本中
        u = list[i]
        with open('E:/taobao.txt', 'a') as data:
            print(u, file=data)


def main():
    goods = '水杯'
    depth = 3   # 定义爬取深度，即翻页处理
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)  # 因为淘宝显示每页44个商品，第一页i=0,一次递增
            html = get_html(url)
            get_data(html, infoList)
        except:
            continue
    write_data(infoList, len(infoList))


if __name__ == '__main__':
    main()