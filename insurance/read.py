import requests
from bs4 import BeautifulSoup


class Txt():
    def __init__(self):
        pass

    # 获取每一章的内容
    def get_chapter_details(self, mUrl):
        r = requests.get(mUrl)
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('div', class_="showtxt")
        htretxt = htre[0].text
        print(htretxt.replace('\xa0' * 8, '\n\n'))
        return htretxt

    # 获取列表
    def get_chapter_list(self,baseUrl,mUrl):
        r = requests.get(mUrl)
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('div', class_="listmain")
        htretxt = str(htre[0])
        ab_f = BeautifulSoup(htretxt)
        ab=ab_f.find_all('a')
        for va in ab:
            print(va.string, baseUrl + va.get('href'))
        return htretxt




if __name__ == '__main__':
    mT = Txt()
    mT.get_chapter_details('https://www.biqukan.com/0_790/71166370.html')

