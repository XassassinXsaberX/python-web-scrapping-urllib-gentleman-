
"""有些網頁，比如登錄的。如果你不是從瀏覽器發起的請求，這就不會給你響應，
這時我們就需要自己來寫header。然後再發給網頁的伺服器，這時它就以為你就是一個正常的瀏覽器。從而就可以爬了！"""

import  urllib.request
weburl =  "http://www.douban.com/"

#自訂一個 http requset  header (用dict物件形式)
webheader = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0' }
req = urllib.request.Request(url=weburl, headers=webheader)#建立一個request 物件
webPage=urllib.request.urlopen(req)  #連線到指定的url，並傳回一個類似檔案物件(file-like object)的物件

data = webPage.read()                #data會是html的byte形式原始碼
data = data.decode( 'UTF-8' )        #將byte形式的原始碼用utf-8編碼方式解碼成人類看得懂的字串

print (data)
print (type(webPage))                #印出<class 'http.client.HTTPResponse'>
print (webPage.geturl())             #印出字串  https://www.douban.com/
print (webPage.info())               #印出伺服器傳回的HTTP response header
print (webPage.getcode())            #http Status Code : 200 (ok)