#出處 http://blog.csdn.net/evankaka/article/details/46849095
import  urllib.request
weburl =  "http://www.douban.com/"
#簡易版的request header
webheader1 = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0' }
#User-Agent  :  我們上網登陸論壇的時候，往往會看到一些歡迎信息，其中列出了你的操作系統的名稱和版本，你所使用的瀏覽器的名稱和版本，
#                       這往往讓很多人感到很神奇，實際上，服務器應用程序就是從User-Agent這個request header field中獲取到這些信息。
#                       User-Agent  request header field允許客戶端將它的操作系統、瀏覽器和其它屬性告訴服務器。
#                       不過，這個request header field不是必需的，如果我們自己編寫一個瀏覽器，不使用User-Agent request header field，那麼服務器端就無法得知我們的信息了。


#複雜版的request header
webheader2 = {
    'Connection' :  'Keep-Alive' ,
    'Accept' :  'text/html, application/xhtml+xml, */*' ,
    'Accept-Language' :  'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3' ,
    'User-Agent' :  'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko' ,
    #'Accept-Encoding': 'gzip, deflate',
    'Host' :  'www.douban.com' ,
    'DNT' :  '1'
    }
#Accept  :
#Accept request header field用於指定客戶端接受哪些類型的信息。eg：Accept：image/gif，表明客戶端希望接受GIF圖像格式的資源；Accept：text/html，表明客戶端希望接受html文本。
#

req = urllib.request.Request(url=weburl, headers=webheader2) #建立一個request 物件
webPage=urllib.request.urlopen(req)                          #連線到指定的url，並傳回一個類似檔案物件(file-like object)的物件
data = webPage.read()                                        #data會是html的byte形式原始碼
data = data.decode( 'UTF-8' )                                #將byte形式的原始碼用utf-8編碼方式解碼成人類看得懂的字串
print (data)
print (type(webPage))          #印出<class 'http.client.HTTPResponse'>
print (webPage.geturl())       #印出 https://www.douban.com/
print (webPage.info())         #印出伺服器傳回的HTTP response header
print (webPage.getcode())      #http Status Code : 200 (ok)