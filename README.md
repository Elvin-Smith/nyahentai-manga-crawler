# nyahentai-manga-crawler
nyahentai漫画爬虫
# 使用说明
1.下载所有文件到一个文件夹nyahentai-manga-crawler
2依赖库安装
```bash
# 首先，确信你的机器安装了 Python 3.8 及以上版本
$ python --version
Python 3.8.13

# 安装依赖
$ pip install requests
$ pip bs4
```
3.使用命令行进入该文件夹
```bash
# 替换为你前面下载到的文件夹，默认为nyahentai-manga-crawler
cd nyahentai-manga-crawler

#运行主文件
python main.py

```

# tag修改
打开search_with_tag文件，将第7行self.tag=""引号内改为自己的TAG
