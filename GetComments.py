import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
import random


#########################################
#########################################

## 设置爬取参数
## pids 为博文参数
## uid 为用户 id
pids = [4765751774544077] # 博文 id
uid = 6570121219 # 微博用户 id


##########################################
##########################################

def fetchUrl(pid, uid, max_id):

    # url
    url = "https://weibo.com/ajax/statuses/buildComments"

    # request_headers
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
    }

    params = {
        "flow": 0,
        "is_reload": 1,
        "id": pid,
        "is_show_bulletin": 2,
        "is_mix": 0,
        "max_id": max_id,
        "count": 20,
        "uid": uid,
    }

    r = requests.get(url, headers=headers, params=params)
    return r.json()


def save_data(data, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)
    dataframe = pd.DataFrame(data)
    dataframe.to_csv(path + filename, encoding='utf_8_sig', mode='a', index=False, sep=',', header=False)


def parseJson(jsonObj):
    data = jsonObj["data"]
    max_id = jsonObj["max_id"]

    commentData = []
    for item in data:
        # 评论id
        comment_Id = item["id"]
        # 评论内容
        content = BeautifulSoup(item["text"], "html.parser").text
        # 评论时间
        created_at = item["created_at"]
        # 点赞数
        like_counts = item["like_counts"]
        # 评论数
        total_number = item["total_number"]

        # 评论者 id，name，city
        user = item["user"]
        userID = user["id"]
        userName = user["name"]
        userCity = user["location"]

        dataItem = [comment_Id, created_at, userID, userName, userCity, like_counts, total_number, content]
        print(dataItem)
        commentData.append(dataItem)

    return commentData, max_id



path = "./comments/"  # 保存评论位置
csvHeader = [["评论id", "发布时间", "用户id", "用户昵称", "用户城市", "点赞数", "回复数", "评论内容"]]

for pid in pids:
    max_id = 0
    filename = 'cmt' + str(pid) + '.csv'
    save_data(csvHeader, path, filename)
    while True:
        time.sleep(random.random() * 3)
        html = fetchUrl(pid, uid, max_id)
        comments, max_id = parseJson(html)
        save_data(comments, path, filename)
        # max_id 为 0 时，表示爬取结束
        if max_id == 0:
            break