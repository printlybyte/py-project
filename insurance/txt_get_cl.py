import requests, sys, re
from bs4 import BeautifulSoup
from Randomwalkpa.pltutf import utfinit

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
        self.names = []  # 存放章节名
        self.urls = []  # 存放章节链接
        self.nums = []  # 章节数
        self.headers = {"Host": "private70.ghuws.win",
                        "Connection": "keep-alive",
                        "Upgrade-Insecure-Requests": "1",
                        "User-Agent": "Mozilla/5.0 (Linux; Android 9; ALP-AL00 Build/HUAWEIALP-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                        "Accept-Encoding": "gzip,deflate",
                        "Accept-Language": "zh-CN,en-GB;q=0.9,zh-TW;q=0.8,en-US;q=0.7",
                        "Cookie": "ismob=1; hiddenface=; __cfduid=d2b601843c2ba00e20696caa0b92c47931532129636; UM_distinctid=16879958dc365-0d08bc2936586a-573c4f3b-38400-16879958dc818c; cssNight=; 227c9_lastvisit=0%091554971930%09%2Fread.php%3Ftid%3D3493208; CNZZDATA950900=cnzz_eid%3D416402323-1532126844-%26ntime%3D1555028696",
                        "X-Requested-With": "com.cl.newt66y"}
        heros_url = "http://private70.ghuws.win/thread0806.php?fid=20&search=&page=1"
        pass

    def get_contents(self, target):
        req = requests.get(url=target)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html,'html.parser')
        texts = bf.find_all('div', class_='tpc_cont')
        texts = texts[0].text.replace('\xa0' * 8, '\n\n')
        # print(texts)
        return texts

    # 获取列表
    def get_chapter_list(self, baseUrl, mUrl):
        req = requests.get(url=mUrl, headers=self.headers)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        htre = bf.find_all('div', class_="list t_one")
        # re.findall(r"前(.+?)后", r.url)
        self.nums.append(len(htre[12:]))
        for key in htre[6:]:
            ab = key.find('a')
            ab_u = key.attrs.get("onclick")
            ab_ur = str(ab_u)
            ab_urs = re.findall(r"window.location='(.+?)';", ab_ur)
            self.names.append(ab.string)
            self.urls.append(baseUrl + ab_urs[0])
            print(ab.string, baseUrl + ab_urs[0])

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
    mT.get_chapter_list('http://private70.ghuws.win/',
                        'http://private70.ghuws.win/thread0806.php?fid=20&search=&page=1')
    mT.get_contents('http://private70.ghuws.win/htm_mob/20/1904/3494015.html')
    print('《x》开始下载：')
    lens=sum(mT.nums)
    print(lens)
    for i in range(lens):
        mT.writer(mT.names[i], 'xxxxxx.txt', mT.get_contents(mT.urls[i]))
        print("已下载:%.3f%%" %  float(i/lens) + '\r')
        sys.stdout.write("  已下载:%.3f%%" %  float(i/lens) + '\r\r\r')
        sys.stdout.flush()
    print('《x》下载完成')