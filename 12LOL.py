import requests
import re
import json

def getlolimages():
    url_js = 'http://lol.qq.com/biz/hero/champion.js'
    html_js = requests.get(url_js).text#返回状态吗 200表示成功
    req = '"keys":(.*?),"data"'
    #req=re.compile(req)# xiaolv
    list_js = re.findall(req,html_js)
    print(list_js[0])
#str  ->dict
    dict_js=json.loads(list_js[0])

#拼接url
    pic_lis=[]
    for hero_id in dict_js:
        #hero id
        #print(hero_id)
#http://ossweb-img.qq.com/images/lol/web201210/skin/big
        for i in range(20):
            num = str(i)
            if len(num) == 1:
                hero_num = "00" + num
            elif len(num) == 2:
                hero_num = "0"+ num
            numste = hero_id + hero_num
            url = 'http://ossweb-img.qq.com/images/lol/web201210/skin/big' + numstr + '.jpg'
            pic_list.append(url)
            # get photo path
            path = r'c:\users\administrator\desktop\demo\LOLPic\\'
            print(dict_js.vlaues())

            for name in dict_js.values():
                print(name)
                for i in range(20):
                    file_path=path + name + str(i) +'.jpg'
                    list_filepath.append(file_path)
            # down photo
            n = 0
            for picurl in pic_list:
                res = requests.get(picurl)
                print(res)
                if res.status_cod == 200:
                    print("downing ：%s"%list_filepath[n])
                    # write bytes
                    f = open()


if __name__=='main':
    getlolimages()


