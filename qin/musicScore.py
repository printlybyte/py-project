import requests
from bs4 import BeautifulSoup


class Qp():
    def __init__(self):
        self.names = []
        self.urls = []
        self.nums = 0
        pass

    # 获取列表
    def get_chapter_list(self, baseUrl, mUrl):
        r = requests.get(mUrl)
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('div', class_="test-txt")
        for va in htre:
            ab = va.find('a')
            print(ab.string)
            print(baseUrl + ab.get('href'))
        # return htretxt

        # PAGES

    def get_page(self,  mUrl):
        r = requests.get(mUrl)
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('div', class_="pagination")
        print(html)
        # for va in htre:
        #     ab = va.find('a')

        # return htretxt



if __name__ == "__main__":
    qp= Qp()
    baseUrl = 'http://www.jitaba.cn/jitapu/list_41_1.html'

    qp.get_page(baseUrl)
    # mUrl = 'https://www.zujuan.com/paper/index?province_id=11&page='
    # mUrlx = '&per-page=10'
    # for va in range (50):
    #     mUrls=mUrl+str(va)+mUrlx
    #     zj.get_chapter_list(baseUrl, mUrls)
        # print(mUrls)
