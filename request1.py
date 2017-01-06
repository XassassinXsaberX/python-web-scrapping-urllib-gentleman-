import urllib.request

response = urllib.request.urlopen("http://acm.hit.edu.cn")
html = response.read()
z_data = html.decode("UTF-8")  # 轉碼後才能看見原來的字符，如漢字，如果不對，試一試“GBK”解碼
print(z_data)

file = open("txt.html", "wb")  # python是types格式，得用二進制讀寫.
file.write(html)
file.close()