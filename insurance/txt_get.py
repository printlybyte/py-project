import requests,sys
from bs4 import BeautifulSoup

"""
类说明:下载《笔趣看》网小说《元尊》
Parameters:
    无
Returns:
    无
Modify:
    20119-04-11
"""


class Txt():
    def __init__(self):
        self.names = []            #存放章节名
        self.urls = []            #存放章节链接
        self.nums = 0            #章节数
        pass


    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts
    # 获取每一章的内容
    def get_chapter_details(self, mUrl):
        r = requests.get(mUrl)
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('div', class_="showtxt")
        try:
            htretxt = htre[0].text

        except ZeroDivisionError:
            print("章节错误")
            return "章节错误"
        else:
            htretxts=htretxt.replace('\xa0' * 8, '\n\n')
            return htretxts

    # 获取列表
    def get_chapter_list(self, baseUrl, mUrl):
        r = requests.get(mUrl)
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('div', class_="listmain")
        htretxt = str(htre[0])
        ab_f = BeautifulSoup(htretxt,"html.parser")
        ab = ab_f.find_all('a')
        self.nums = len(ab[12:])
        for va in ab[12:]:
            mUrl=baseUrl + va.get('href')
            print(va.string, mUrl)
            self.names.append(va.string)
            self.urls.append(mUrl)

        return htretxt

    """
   函数说明:将爬取的文章内容写入文件
   Parameters:
       name - 章节名称(string)
       path - 当前路径下,小说保存名称(string)
       text - 章节内容(string)
   Returns:
       无
   Modify:
       2017-09-13
   """

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    mT = Txt()
    mT.get_chapter_list('https://www.biqukan.com/', 'https://www.biqukan.com/0_790/')
    # mT.get_chapter_details('https://www.biqukan.com/0_790/71166370.html')
    print('《元尊》开始下载：')
    for i in range(mT.nums):
        mT.writer(mT.names[i], '元尊.txt', mT.get_chapter_details(mT.urls[i]))
        print("  已下载:%.3f%%" %  float(i/mT.nums) + '\r')
        sys.stdout.write("  已下载:%.3f%%" %  float(i/mT.nums) + '\r')
        sys.stdout.flush()
    print('《元尊》下载完成')
