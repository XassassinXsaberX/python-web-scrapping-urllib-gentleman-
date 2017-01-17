import urllib.request
import webbrowser

response = urllib.request.urlopen("http://acm.hit.edu.cn")  #連線到指定的url，並傳回一個類似檔案物件(file-like object)的物件
html = response.read()          #html會參考到byte形式的網頁原始碼
z_data = html.decode("UTF-8")  #解碼後才能看見原來的字串
print(z_data)                   #印出該網頁的原始碼
with open("txt.html","wb") as file:
    file = open("txt.html", "wb")   # python是types格式，得用二進制讀寫.
    file.write(html)                #將html原始碼資料寫入自訂的txt.html檔中

webbrowser.open("txt.html")      #利用webbrowser打開瀏覽器流覽指定url

