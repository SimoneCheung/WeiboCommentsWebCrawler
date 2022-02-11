# WeiboCommentsWebCrawler
用来爬取指定微博博文评论

## 使用方法
更改 01GetWeiboCommets.py 文件中的 id 和 pids 即可。

注意可能还需要改其中 fetchUrl() 函数的 headers 参数。

具体如何获取所需参数，可看我的博客文章[明天写]()。

改完参数后，依次运行 01.py, 02.py, 03.py 即可获取词云图。

测试时间 2022 年 2 月 11 日。

代码部分有效，我也不知道原因，01 代码运行了若干小时后中断报错，但数据确实保存了下来。

## 参考文献

- [Python 爬虫实战：手把手教你爬取微博评论](https://mp.weixin.qq.com/s/ON97bDKrDHWOOjiuBfY42g)
- [pyecharts 官方教程](https://gallery.pyecharts.org/#/WordCloud/wordcloud_custom_mask_image)

特别致谢，感谢[Python 爬虫实战：手把手教你爬取微博评论](https://mp.weixin.qq.com/s/ON97bDKrDHWOOjiuBfY42g)的作者（微信昵称 机灵鹤）的指导。


