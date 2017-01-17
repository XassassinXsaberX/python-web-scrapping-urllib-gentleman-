import sys
import urllib.request
import urllib.error

req = urllib.request.Request('http://www.python.org/fish.html')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)         #HTTP status code
    print(e.headers)      #印出 HTTP response headers
    print(e)              #印出 HTTP Error 404: OK
    print(e.read())       #印出網頁錯誤資訊的html檔
except urllib.error.URLError as e:
    print(e)
    print(e.reason)       #The reason for this error. It can be a message string or another exception instance

