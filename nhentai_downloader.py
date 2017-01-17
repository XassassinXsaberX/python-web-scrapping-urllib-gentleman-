#coding="utf-8"
import re,os,threading
import urllib.request

def find_dir_title(url,html):#從網頁原始碼中找尋標題
    if "nhentai" in url:
        image_url = re.findall(r'<div id="info">[\w\W]+?</h2>', html)
        dir_name = "./" + image_url[0].split("<h2>")[1][:-5]
    elif "wnacg" in url:
        image_url = re.findall(r'<title>.+?</title>',html)
        dir_name = "./" + image_url[0].split("<title>")[1]
        dir_name = dir_name.split(" - 紳士漫畫")[0]
    return dir_name

def find_image_url(url,html):#從main網頁中找尋圖片url
    if "nhentai" in url:
        image_url = re.findall(r'(<img src=".+?.(jpg|png|gif))" width', html)
        lt = [0]*len(image_url)
        for i in range(len(image_url)):
            lt[i] = image_url[i][0]
        image_url = lt
        for i in range(len(image_url)):
            image_url[i] = image_url[i].split('<img src="')[1]
            if 'jpg' in image_url[i]:
                image_url[i] = image_url[i].split('t.jpg')[0]
                image_url[i] = "https:" + image_url[i] + ".jpg"
            elif 'png' in image_url[i]:
                image_url[i] = image_url[i].split('t.png')[0]
                image_url[i] = "https:" + image_url[i] + ".png"
            else:
                image_url[i] = image_url[i].split('t.gif')[0]
                image_url[i] = "https:" + image_url[i] + ".gif"

        return image_url #回傳一個list，其中每一個元素都是圖片的url
    elif "wnacg" in url:
        #找取圖片的名稱
        def next_web_page(url,image_name,error,lock):#該函式的功用是找取圖片的真實名稱
            """url為網址，image_name用來存放圖片名稱，error用來告訴這個thread是否要終止，lock為互斥鎖"""
            #要先連到特定網頁才能擷取該網頁的圖片名稱
            webheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            req = urllib.request.Request(url=url, headers=webheader)
            web = urllib.request.urlopen(req)
            lt = re.findall(r'<span class="name">.+?<',web.read().decode("utf-8"))# lt 現在存放圖片的名稱，但要在整理一下才行
            with lock:
                for i in range(len(lt)):
                    lt[i] = lt[i].split("<span class=\"name\">")[1][:-1]
                    if lt[i] in image_name:
                        break
                    image_name.append(lt[i])

        target_url = [0]*200
        image_name = []#用來存放圖片的名稱
        thread = [0]*len(target_url)
        error = [0]
        lock = threading.Lock()
        for i in range(1,len(target_url)):
            target_url[i] = url.split("index")[0] + "index-page-{0}".format(i) + url.split("index")[1]
            thread[i] = threading.Thread(target=next_web_page,args=(target_url[i],image_name,error,lock))
            thread[i].start()
        for i in range(1,len(target_url)):
            thread[i].join()



        #先找取圖片網頁的進入點
        input_url = re.findall(r'<div class="pic_box"><a href=".+?.html',html)
        input_url = input_url[0].split("<a href=\"")[1]
        input_url = "http://www.wnacg.com/" + input_url
        webheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=input_url, headers=webheader)
        web = urllib.request.urlopen(req)
        html = web.read().decode("utf-8")

        #接下來可以從此html原始碼中找真正要抓的圖片url了
        image_url = re.findall(r'src="/data.+?\.jpg',html)
        image_url = image_url[0].split("src=\"")[1]
        for i in range(-1,-100,-1):
            if image_url[i] == '/':
                image_url = image_url[0:i+1]
                break
        image_url = "http://www.wnacg.com" + image_url
        lt = image_url
        image_url = [0]*len(image_name)
        for i in range(len(image_name)):
            image_url[i] = lt + "{0}.jpg".format(image_name[i])
        return image_url

def downloader(i, dir_name, url,count,total,lock):

    urllib.request.urlretrieve(url, "{0}\{1}.jpg".format(dir_name, i))
    with lock:
        print("圖片{0}.jpg 已下載完成".format(i),end=" ")
        count[0] += 1
        print("已下載{0}/{1}張圖".format(count[0],total))


if __name__ == "__main__":
    try:
        #url = input("請輸入網頁")
        #url = "https://nhentai.net/g/128414/"
        #url = "http://www.wnacg.com/photos-index-aid-35197.html"
        #url = "http://www.wnacg.com/photos-index-aid-35188.html"
        url = 'https://nhentai.net/g/128414/'
        #url = "http://www.wnacg.com/photos-index-aid-21037.html"           #bug need to fix





        #建立連線並下載網頁原始碼
        webheader = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0' }
        req = urllib.request.Request(url=url, headers=webheader)
        webpage = urllib.request.urlopen(req)
        html = webpage.read().decode("utf-8")

        #從網頁原始碼中尋找標題
        dir_name = find_dir_title(url,html)

        #獲取一個list，其中的元素為圖片的url
        image_url = find_image_url(url,html)

        #建立一個資料夾
        try:
            if not os.path.exists(dir_name):
                os.mkdir(dir_name)
        except OSError as e:
            while True:
                print("無法順利建立資料夾:{}，請重新命名".format(dir_name))
                dir_name = input("請輸入資料夾名稱:")
                try:
                    os.mkdir(dir_name)
                except:
                    continue
                else:
                    break



        #接下來可以下載圖片
        print("開始下載圖片...")
        thread = [0]*len(image_url)
        lock = threading.Lock()
        count = [0]
        for i in range(len(image_url)):
            try:
                #print("正在下載圖片{0}.jpg".format(i + 1))
                #web_image = urllib.request.urlretrieve(image_url[i],"{0}/{1}.jpg".format(dir_name,i+1))
                for j in range(-1,-100,-1):
                    if image_url[i][j] == '/':
                        name = image_url[i][j+1:-4]
                        break
                thread[i] = threading.Thread(target=downloader,args=(name,dir_name,image_url[i],count,len(image_url),lock))
                thread[i].start()
            except:
                break
        print("total",len(thread))
        for i in range(len(image_url)):
            thread[i].join(1)
        input("下載完成")
        count = 0
    except BaseException as e:
        print("請將此python設為預設開啟程式才能執行，不能用右鍵->開啟檔案->python執行")
        input()









