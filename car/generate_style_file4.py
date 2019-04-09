import os
from selenium import webdriver

'''
    第四步，浏览器执行第二步生成的html文件，抓取执行结果，保存到本地。
'''
class Crack():
    def __init__(self,keyword,username,passod):
        self.url = 'https://www.baidu.com'
        self.browser = webdriver.Chrome('d:\chromedriver.exe')

if __name__=="__main__":
    lists = os.listdir("e:/car/autoHome/newHtml/")
    crack = Crack('测试公司','17610177519','17610177519')
    for fil in lists:
        file = os.path.exists("e:\\car\\autoHome\\content\\"+fil)
        if file :
            print('文件已经解析。。。'+str(file))
            continue
        print(fil)
        crack.browser.get("file:///e:/car/autoHome/newHtml/"+fil+"")
        text = crack.browser.find_element_by_tag_name('body')
        print(text.text)
        f = open("e:\\car\\autoHome\\content\\"+fil,"a",encoding="utf-8")
        f.write(text.text)
    else:
        f.close()
        crack.browser.close()