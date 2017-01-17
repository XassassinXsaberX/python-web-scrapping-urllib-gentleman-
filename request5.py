import  urllib.request
import  socket
import  re
import  sys
import  os
targetDir = r"D:\PythonWorkPlace\load" #文件保存路徑
def  destFile(path):
    if not  os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex( '/' )
    t = os.path.join(targetDir, path[pos+ 1 :])
    return  t
if  __name__ ==  "__main__" :   #程序運行入口
    weburl =  "http://www.douban.com/"
    webheaders = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0' }
    req = urllib.request.Request(url=weburl, headers=webheaders)   #構造請求報頭
    webpage = urllib.request.urlopen(req)   #發送請求報頭
    contentBytes = webpage.read()
    for link, t  in set(re.findall(r'(http:[^\s]*?(jpg|png|gif))' , str(contentBytes))):   #正則表達式查找所有的圖片
        print (link)
        try :
            urllib.request.urlretrieve(link, destFile(link))  #下載圖片
        except :
            print ( '失敗' )  #異常拋出