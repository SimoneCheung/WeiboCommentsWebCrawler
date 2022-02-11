import os
import csv


for filename in os.listdir("../comments"):
    i = 0
    # print(filename)
    if filename[:3] == "cmt":
        csv_reader = csv.reader(open('../comments/' + filename, encoding="utf8"))
        with open("../comments/weibocmt.csv", 'a', encoding="utf8") as cmt:
            for row in csv_reader:
                i = i + 1
                if i == 1:
                    continue
                cmt.write(row[-1])