import os
import urllib

import requests
from bs4 import BeautifulSoup


class Qp():
    def __init__(self):
        self.names = []
        self.urls = []
        self.nums = 0

        self.headers = {"Content-Encoding": "gzip, deflate",
                        "Connection": "keep-alive",
                        "Host": "www.jitaba.cn",
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
                        "Upgrade-Insecure-Requests": "1",
                        "Referer": "http://www.jitaba.cn/jitapu/list_41_425.html",
                        "Content-Type": "text/html",
                        "Cookie": "bdshare_firstime=1556970879628; Hm_lvt_0852c877dac3dce47c4be57c9eff5656=1556970880; Hm_lpvt_0852c877dac3dce47c4be57c9eff5656=1556971049; __tins__1209496=%7B%22sid%22%3A%201556972881293%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201556974696968%7D; __51cke__=; __51laig__=7",
                        "Accept-Language": "zh-CN,zh;q=0.8",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                        }
        pass

        # def get_img(self, url):
        #     path = 'E:\\image' + '\\' + url.split('/')[-1]
        #     print(path)
        #     filename = url.split('/')[-1]
        #     img_path = path + '\\' + filename
        #     img = requests.get(url)
        #     try:
        #         with open(img_path, 'wb') as f:
        #             f.write(img.content)
        #     except:
        #         pass

    def get_img(self, url):
            print(url)
            filename = url.split('/')[-1]
            global path
            img_path = path + '\\' + filename
            img = requests.get(url, headers=self.headers)
            try:
                with open(img_path, 'wb') as f:
                    f.write(img.content)
            except:
                pass

    # 获取图片
    def get_img_list(self, mUrl):
        req = requests.get(url=mUrl, headers=self.headers)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('div', class_="tabbox1")
        bfx = BeautifulSoup(str(htre), 'html.parser')
        htrex = bfx.find_all('img')
        # print(htrex)
        for va in htrex:
            sub_url=va.get('src')
            # self.get_img(sub_url)
            print(sub_url)

    # 获取列表
    def get_chapter_list(self, mUrl):
        req = requests.get(url=mUrl, headers=self.headers)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('a', class_="STYLE3")
        for va in htre:
            print(va.string, va.get('href'))
            global path
            path = 'E:\\image' + '\\' + va.string
            os.mkdir(path)
            self.get_img_list(va.get('href'))
        # return htretxt

    def get_page(self, mUrl):
        req = requests.get(url=mUrl, headers=self.headers)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find('span', class_="pageinfo")
        m_name = htre.find("strong")
        print(m_name.string)
        return m_name.string


if __name__ == "__main__":
    qp = Qp()
    baseUrl = 'http://www.jitaba.cn/jitapu/list_41_1.html'
    startUrl = 'http://www.jitaba.cn/jitapu/list_41_'
    endUrl = '.html'

    pages = qp.get_page(baseUrl)
    print(pages)
    # for va in range(0,int(pages)):
    for va in range(1, 2):
        mBaseUrl = startUrl + str(va) + endUrl
        qp.get_chapter_list(mBaseUrl)
        print(mBaseUrl)

    # # qp.get_chapter_list('http://www.jitaba.cn/jitapu/list_41_1.html')
    # qp.get_img_list('http://www.jitaba.cn/pu/pinguan/11649.html')
