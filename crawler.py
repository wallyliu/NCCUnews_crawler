# -*- coding:utf-8 -*-
import requests, time
import codecs
from bs4 import BeautifulSoup

link = 'http://www.nccu.edu.tw/zh_tw/news/'
res = requests.get(link)
soup = BeautifulSoup(res.text)

# 記錄新聞的頁面總共有幾個page並存在pageNum中
for element in soup.select('a'):
    if element.text == "Last":
        last = element
        pageNum = last['href'][9:12]

# 把所有要下載的連結儲存到list:feedLink中以備crawler使用
feedLink = []
for i in range(1, int(pageNum)+1):
    feedLink.append( link + "?page_no=" + str(i) )

# 用cnt變數紀錄新聞總量(除了最後一頁外, 每頁10個), 以新聞出現的順序1,2,3..依序為檔名
feedback = requests.get(feedLink[len(feedLink)-1])
soup = BeautifulSoup(feedback.text)
cnt = (int(pageNum) - 1) * 10 + len(soup.select('.i-news__link'))

# 開始爬資料
for i in feedLink:
    feedback = requests.get(i)
    soup = BeautifulSoup(feedback.text)

    # 建立連結並爬資料, 每次爬一頁
    for element in soup.select('.i-news__link'):
        alink = 'http://www.nccu.edu.tw' + element['href']
        r = requests.get(alink)
        r = BeautifulSoup(r.text)

        # 將文章標題儲存到變數title
        title = r.select('.primary')[0].select('span')[0].text

        # 將文章內容儲存到變數content
        tmp = r.select('.primary')[0].select('p')
        tmp = tmp[1:]
        content = ''
        for element in tmp:
            content += element.text

        # 把爬下來的內容寫入txt檔
        t = "news" + str(cnt) + ".txt"
        cnt -= 1
        t = codecs.open(t, 'w', "utf-8")
        t.write(title)
        t.write("\n")
        t.write(content)
        t.write("\n")
        t.close()
