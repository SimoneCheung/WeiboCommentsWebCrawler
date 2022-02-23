import os
import csv
import jieba
from pyecharts.charts import WordCloud


for filename in os.listdir("./comments"):
    i = 0
    # print(filename)
    if filename[:3] == "cmt":
        csv_reader = csv.reader(open('./comments/' + filename, encoding="utf8"))
        with open("./comments/weibocmt.csv", 'a', encoding="utf8") as cmt:
            for row in csv_reader:
                i = i + 1
                if i == 1:
                    continue
                cmt.write(row[-1])


## 先汇总评论 再词频统计 最后绘制全部词语的词云
txt = open("./comments/weibocmt.csv", mode='r', encoding="utf8")
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
wc.add(series_name="WordCloudAndFrequency", data_pair=items)
wc.render("./comments/WB_cmt_WordCloud.html")