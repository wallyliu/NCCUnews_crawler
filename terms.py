# -*- coding: utf8 -*-

# 建議每次跑2000筆檔案左右分成四次跑(結果也分成四個檔案)後, 再用另一支程式將所有結果合併
# 因此使用前需更改第13行(要抓進來計算的檔名)與第40行參數(儲存terms結果的檔名)

import jieba
import operator

# 把所有檔案路徑儲存到list:fileList
filepath = "news/news"
fileList = []
for i in range(6000,7074):
    fileList.append( filepath + str(i) + ".txt")

# 利用結巴系統斷詞,並將斷詞結果存到list:word中
word = []
for link in fileList:
    src = open(link, 'r').read()
    src = src.decode('utf8')
    words = jieba.cut( src, cut_all=False)
    for i in words:
        word.append(i)

# 建立terms並計算數量
word.sort()
index = [[' ']]
for i in word:
    if i != index[len(index)-1][0]:
        index.append([i])
        index[len(index)-1].append(int(1))
    else:
        index[len(index)-1][1] += 1
index.pop(0)

index.sort(lambda x, y:cmp(x[1], y[1]), reverse=True)


# 把計算後結果寫入檔案
f = open('./index/index4.txt', 'w')
for i in index:
    f.write(i[0].encode('utf8'))
    f.write("{}")
    f.write(str(i[1]))
    f.write("@@")
