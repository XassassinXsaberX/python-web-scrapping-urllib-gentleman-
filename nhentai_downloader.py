#coding="utf-8"
import re,os
import urllib.request

url = input("請輸入網頁")
#url = "https://nhentai.net/g/183710/"

webheader = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0' }
req = urllib.request.Request(url=url, headers=webheader)
webpage = urllib.request.urlopen(req)
html = webpage.read().decode("utf-8")
image_url = re.findall(r'<div id="info">[\s]*.*[\s]*.*]',html)
dir_name = "./"+image_url[0].split("<h2>")[1]

#尋找圖片名稱
image_url = re.findall(r'<img src=".+?.jpg" width',html)
for i in range(len(image_url)):
    image_url[i] = image_url[i].split('<img src="')[1]
    image_url[i] = image_url[i].split('t.jpg" width')[0]
    image_url[i] = "https:" + image_url[i] + ".jpg"

#建立一個資料夾
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

#接下來可以下載圖片
for i in range(10000):
    try:
        web_image = urllib.request.urlretrieve(image_url[i],"{0}/{1}.jpg".format(dir_name,i+1))
    except:
        break




