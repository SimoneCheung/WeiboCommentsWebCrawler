import jieba
from pyecharts.charts import WordCloud


txt = open("../comments/weibocmt.csv", mode='r', encoding="utf8")
text = txt.readlines()
txt.close()

jieba.add_word("米哈游")
words = jieba.lcut(str(text))
excludes = []
counts = {}
for word in words:
    if len(word) == 1:
        continue
    counts[word] = counts.get(word, 0) + 1

for word in excludes:
    del(counts[word])

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

wc = WordCloud()
wc.add(series_name="WordCloud", data_pair=items)
wc.render("../comments/WB_cmt_WordCloud.html")