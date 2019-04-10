import requests
from bs4 import BeautifulSoup


class Txt():
    def __init__(self):
        pass

    # 获取每一种酒的内容
    def get_chapter_details(self, mUrl):
        r = requests.get(mUrl)
        # r = requests.get("http://www.vatsliquor.com/Marketing/Product/Domestic/maotai/2019/0128/277.html")
        r.encoding = 'utf-8'  # 需要添加这一行，告知html文件解码方式
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('div',  ['cpxqs_right','cpxqs_cont'])
        htretxt = htre[0].text
        htretxt2 = htre[1].text
        print(htretxt.replace('\xa0' * 8, '\n\n'))
        print(htretxt2 )
        return htretxt

    # 获取列表
    def get_chapter_list(self, baseUrl, mUrl):
        r = requests.get(mUrl)
        r.encoding = 'utf-8'  # 需要添加这一行，告知html文件解码方式
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('ul', class_="ppxq_list_u2")
        htretxt = str(htre[0])
        ab_f = BeautifulSoup(htretxt, 'html.parser')
        ab = ab_f.find_all('a')
        for va in ab:
            ap_title = va.find('p')
            ap_img = va.find('img')
            details_url=baseUrl + va.get('href')
            print(details_url, ap_title.string, baseUrl + ap_img.get('src'))
            self.get_chapter_details(details_url)
        return htre

    # 获取主标题列表
    def get_chapter_title_list(self, baseUrl, mUrl):
        r = requests.get(mUrl)
        r.encoding = 'utf-8'  # 需要添加这一行，告知html文件解码方式
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('ul', class_="ppxq_list_u1")
        htretxt = str(htre[0])
        ab_f = BeautifulSoup(htretxt,'html.parser')
        ab = ab_f.find_all('a')
        for va in ab:
            # print(va.string, baseUrl + va.get('href'))
            mSpuilt=baseUrl + va.get('href')
            self.get_chapter_list("http://www.vatsliquor.com",
                                  mSpuilt)
            print('\n')
        return htre


if __name__ == '__main__':
    mT = Txt()
    # mT.get_chapter_details("")
    # mT.get_chapter_details('https://www.biqukan.com/0_790/71166370.html')
    # mT.get_chapter_list("http://www.vatsliquor.com",
    #                     'http://www.vatsliquor.com/Marketing/Product/Domestic/maotai/')

    mT.get_chapter_title_list("http://www.vatsliquor.com",
                              'http://www.vatsliquor.com/Marketing/Product/Domestic/maotai/')
    mT.get_chapter_title_list("http://www.vatsliquor.com",
                              'http://www.vatsliquor.com/Marketing/Product/international/first/Aaron/alunxuan_putaojiu/')
    mT.get_chapter_title_list("http://www.vatsliquor.com",
                          'http://www.vatsliquor.com/Marketing/Product/international/Mingzhuang/Bordeaux/boerduoliejimingzhuang/')
    mT.get_chapter_title_list("http://www.vatsliquor.com",
                          'http://www.vatsliquor.com/Marketing/Product/international/Spirits/Garstein/')

