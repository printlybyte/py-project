import os
import re
'''
第五步 匹配样式文件与json数据文件，生成正常的数据文件。
'''
if __name__ =="__main__":
    rootPath = "e:\\car\\autoHome\\json\\"
    listdir = os.listdir(rootPath)
    for json_s in listdir:
        print(json_s.title())
        jso = ""
        #读取json数据文件
        for fi in open(rootPath+json_s,'r',encoding="utf-8"):
            jso = jso+fi
        content = ""
        #读取样式文件
        spansPath = "e:\\car\\autoHome\\content\\"+json_s.title()+".html"
        # print(spansPath)
        for spans in  open(spansPath,"r",encoding="utf-8"):
            content = content+ spans
        print(content)
        #获取所有span对象
        jsos = re.findall("<span(.*?)></span>",jso)
        num = 0
        for js in jsos:
            print("匹配到的span=>>"+js)
            num = num +1
            #获取class属性值
            sea = re.search("'(.*?)'",js)
            print("匹配到的class==>"+sea.group(1))
            spanContent = str(sea.group(1))+"::before { content:(.*?)}"
            #匹配样式值
            spanContentRe = re.search(spanContent,content)
            if spanContentRe != None:
                if sea.group(1) != None:
                    print("匹配到的样式值="+spanContentRe.group(1))
                    jso = jso.replace(str("<span class='"+sea.group(1)+"'></span>"),re.search("\"(.*?)\"",spanContentRe.group(1)).group(1))
        print(jso)
        fi = open("e:\\car\\autoHome\\newJson\\"+json_s.title(),"a",encoding="utf-8")
        fi.write(jso)
        fi.close()