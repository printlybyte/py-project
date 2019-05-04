import requests
from bs4 import BeautifulSoup
import xlwt



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
        detailsx=htretxt.replace('\xa0' * 8, '\n\n')
        details.append(detailsx)
        details2.append(htretxt2)
        print(detailsx)
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
            names.append(ap_title.string)
            address.append(details_url)
            imgs.append( baseUrl + ap_img.get('src'))
            self.get_chapter_details(details_url)


        return names


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

    # 创建workbook（其实就是excel，后来保存一下就行）
    workbook = xlwt.Workbook(encoding='ascii')
    # 创建表
    worksheet = workbook.add_sheet('My Worksheet')
    names,imgs,details,details2,address=[],[],[],[],[]


    mT.get_chapter_title_list("http://www.vatsliquor.com",
                              'http://www.vatsliquor.com/Marketing/Product/Domestic/maotai/')
    mT.get_chapter_title_list("http://www.vatsliquor.com",
                              'http://www.vatsliquor.com/Marketing/Product/international/first/Aaron/alunxuan_putaojiu/')
    mT.get_chapter_title_list("http://www.vatsliquor.com",
                          'http://www.vatsliquor.com/Marketing/Product/international/Mingzhuang/Bordeaux/boerduoliejimingzhuang/')
    mT.get_chapter_title_list("http://www.vatsliquor.com",
                          'http://www.vatsliquor.com/Marketing/Product/international/Spirits/Garstein/')

    for i in range (0,len(names)):
        worksheet.write(i, 0, label=names[i])
        worksheet.write(i, 1, label=address[i])
        worksheet.write(i, 2, label=imgs[i])
        worksheet.write(i, 3, label=details[i])
        worksheet.write(i, 4, label=details2[i])
    workbook.save('Excel_Workbook.xls')

