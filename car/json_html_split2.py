import os
import re
'''
第二步，解析出每个车型的关键js拼装成一个html
'''
if __name__=="__main__":
    print("Start...")
    rootPath = "e:\\car\\autoHome\\html\\"
    files = os.listdir(rootPath)
    for file in files:
        print("fileName=="+file.title())
        text = ""
        for fi in open(rootPath+file,'r',encoding="utf-8"):
            text = text+fi
        else:
            print("fileName=="+file.title())
        #解析数据的json
        alljs = ("var rules = '2';"
                 "var document = {};"
                 "function getRules(){return rules}"
                 "document.createElement = function() {"
                 "      return {"
                 "              sheet: {"
                 "                      insertRule: function(rule, i) {"
                 "                              if (rules.length == 0) {"
                 "                                      rules = rule;"
                 "                              } else {"
                 "                                      rules = rules + '#' + rule;"
                 "                              }"
                 "                      }"
                 "              }"
                 "      }"
                 "};"
                 "document.querySelectorAll = function() {"
                 "      return {};"
                 "};"
                 "document.head = {};"
                 "document.head.appendChild = function() {};"

                 "var window = {};"
                 "window.decodeURIComponent = decodeURIComponent;")
        try:
            js = re.findall('(\(function\([a-zA-Z]{2}.*?_\).*?\(document\);)', text)
            for item in js:
                alljs = alljs + item
        except Exception as e:
            print('makejs function exception')


        newHtml = "<html><meta http-equiv='Content-Type' content='text/html; charset=utf-8' /><head></head><body>    <script type='text/javascript'>"
        alljs = newHtml + alljs+" document.write(rules)</script></body></html>"
        f = open("e:\\car\\autoHome\\newhtml\\"+file+".html","a",encoding="utf-8")
        f.write(alljs)
        f.close()