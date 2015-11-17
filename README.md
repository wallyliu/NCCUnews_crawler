# NCCUnews_crawler
此程式用來抓取政大所有新聞，並利用結巴系統斷詞後，計算出新聞中字詞出現的頻率。\n
執行程式前，需要先安裝以下套件:(可透過pip安裝) 
BeautifulSoup
<pre>
pip install BeautifulSoup
</pre>
Jieba
<pre>
pip install jieba
</pre>

crawler.py：抓取政大的所有新聞，並將每一條新聞儲存成一個檔案。\n
terms.py：分批抓取檔案，並計算斷詞後的term出現數目，並分批儲存到index檔案中。\n
integrateTerm.py：將terms整理出來的數目合併，最後輸出所有字詞結果。\n