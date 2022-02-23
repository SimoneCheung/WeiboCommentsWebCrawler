# WeiboCommentsWebCrawler
## 功能
爬取**指定微博**的评论，并绘制全部评论的词云。

## 使用方法
更改 GetComments.py 文件中第 15 至 19 行的 pids 和 uid 即可。

注意可能还需要改其中 fetchUrl() 函数的 headers 参数。

具体如何获取所需参数，可看我的博客文章[爬取并分析微博评论](https://zmxiehhh.github.io/2022-02-12-wbWebCrawl/)。

改完参数后，依次运行 GetComments.py 和 DrawWC.py 即可获取词云图。

测试时间 2022 年 2 月 23 日。

代码部分有效，我也不知道原因，GetComments.py 代码运行了若干小时后中断报错，但数据确实保存了下来。

## 参考文献

- [Python 爬虫实战：手把手教你爬取微博评论](https://mp.weixin.qq.com/s/ON97bDKrDHWOOjiuBfY42g)
- [pyecharts 官方教程](https://gallery.pyecharts.org/#/WordCloud/wordcloud_custom_mask_image)

特别致谢，感谢[Python 爬虫实战：手把手教你爬取微博评论](https://mp.weixin.qq.com/s/ON97bDKrDHWOOjiuBfY42g)的作者（微信昵称 机灵鹤）的指导。


