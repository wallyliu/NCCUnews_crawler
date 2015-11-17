# -*- coding: utf-8 -*-

# 建立檔案名稱
filepath = 'index'
fileList = []
for i in range(1, 4):
    fileList.append(filepath + str(i) + ".txt")

# 讀取所有紀錄term的檔案,並放入term
index = []
for link in fileList:
    src = open( link, 'r').read().decode('utf8')
    tmp = src.split("@@")
    for i in tmp:
        index.append(i.split("{}"))

# 前處理,把小於2以及的拿掉
index.sort()
cnt = 0

# 移除長度不為2的
for i in range(len(index)):
    if len(index[i]) != 2:
        index[i].pop()
        cnt += 1
index.sort()
for i in range(cnt):
    index.pop(0)

# 把相同的term合併
result = [['A','A']]

for i in index:
    if i[0] == result[len(result)-1][0]:
        result[len(result)-1][1] += int(i[1].encode('utf8'))
    else:
        result.append(i)
        result[len(result)-1][1] = int(result[len(result)-1][1].encode('utf8'))
result.pop(0)

result.sort(lambda x, y:cmp(x[1], y[1]), reverse=True)

# 輸出結果
for i in result:
    print i[0], " ", i[1]
