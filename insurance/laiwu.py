import requests, sys
from bs4 import BeautifulSoup


class fangjia():

    # 获取莱芜年份列表
    def get_chapter_list(self, baseUrl, mUrl):
        r = requests.get(mUrl)
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('div', class_="main-content")
        # htretxt = str(htre[0])
        print(htre)
        # ab_f = BeautifulSoup(htretxt, "html.parser")
        # ab = ab_f.find('switch-year-ajkcomp clearfix')
        # print(ab)
        # self.nums = len(ab[12:])
        # for va in ab[12:]:
        #     mUrl = baseUrl + va.get('href')
        #     print(va.string, mUrl)
        #     self.names.append(va.string)
        #     self.urls.append(mUrl)

        # return htretxt


if __name__ == "__main__":
    mUrl = "https://www.anjuke.com/fangjia/laiwu2015/"
    fj = fangjia();
    fj.get_chapter_list("",mUrl)
    pass
