
import urllib.request
import urllib.parse
import webbrowser


url = 'http://pythonprogramming.net';
values = {'s':'basic',
          'q':'numpy'}; #參數及參數值
data = urllib.parse.urlencode(values);    #解析並轉為url編碼格式
data = data.encode('utf-8');                #將所有網址用utf8解碼
print(data)
req = urllib.request.Request(url, data);   #建立請求
resp = urllib.request.urlopen(req); #開啟網頁
respData = resp.read();

with open("txt.html","wb") as f:
    f.write(respData)

webbrowser.open("txt.html")


"""
try:
    url = 'https://www.google.com.tw/search?q=python';
    #url = 'https://www.google.com.tw/#q=python'; #雖然在google網址上看到搜尋時是這個方式，但是實際操作起來是不成功的
    headers = {};
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17';
    #headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0';
    req = urllib.request.Request(url, headers=headers);
    resp = urllib.request.urlopen(req);
    respData = resp.read()
    saveFile = open('withHeaders.html','wb');
    saveFile.write(respData);
    saveFile.close();
    webbrowser.open("withHeaders.html")
except Exception as e:
    print(str(e));

"""