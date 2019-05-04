import requests
from bs4 import BeautifulSoup
import xlwt

class down_img_C():
    def __init__(self):
        pass
    # 获取列表
    def get_chapter_list(self, mUrl):
        r = requests.get(mUrl)
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('div', class_="yVU8k")
        # htre
        htretxt = str(htre[5])
        print(htre,len(htre))
        ab_f = BeautifulSoup(htretxt,"html.parser")
        ab = ab_f.find('img')
        print(ab.get('src'))
        # self.nums = len(ab[12:])
        # for va in ab[12:]:
        #     mUrl=baseUrl + va.get('href')
        #     print(va.string, mUrl)
        #     self.names.append(va.string)
        #     self.urls.append(mUrl)
        # return htretxt

if __name__=="__main__" :
    mImg=down_img_C()
    mImg.get_chapter_list("https://unsplash.com/t/health")
    pass