# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
class doutuSpider(object):
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}
    def get_url(self,url):
        data = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(data.content,'html.parser')
        totals = soup.findAll("a", {"class": "list-group-item"})
        for one in totals:
            sub_url = one.get('href')
            global path
            path = 'E:\\image'+'\\'+sub_url.split('/')[-1]
            os.mkdir(path)
            try:
                self.get_img_url(sub_url)
            except:
                pass

    def get_img_url(self,url):
        # print(url)
        data = requests.get(url,headers = self.headers)
        soup = BeautifulSoup(data.content, 'html.parser')
        totals = soup.find_all('div',{'class':'artile_des'})
        for one in totals:
            img = one.find('img')
            try:
                sub_url = img.get('src')
            except:
                pass
            finally:
                urls =   sub_url
            try:
                self.get_img(urls)
                self.chunk_download(urls)

            except:
                pass

    def get_img(self,url):
        print(url)
        filename = url.split('/')[-1]
        global path
        img_path = path+'\\'+filename
        img = requests.get(url,headers=self.headers)
        try:
            with open(img_path,'wb') as f:
                f.write(img.content)
        except:
            pass



    # def chunk_download(self, url):
    #     r = requests.get(url, stream=True)
    #     filename = url.split('/')[-1]
    #     with open(filename, 'wb') as f:
    #         for chunk in r.iter_content(chunk_size=32):
    #             f.write(chunk)




    def create(self):
        for count in range(2, 3):
            url = 'https://www.doutula.com/article/list/?page={}'.format(count)
            print ('开始下载第{}页'.format(count))
            self.get_url(url)


if __name__ == '__main__':
    doutu = doutuSpider()
    doutu.create()