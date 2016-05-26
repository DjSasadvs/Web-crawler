# Web-crawler
Use Scrapy to realize the web crawler

This project uses the Scrapy framework to realize the crawler.

### Ref documentation - recommand you read
* [Scrapy 1.1-zh](http://scrapy-chs.readthedocs.io/zh_CN/latest/intro/tutorial.html) 
* [Scrapy 1.1-en](http://doc.scrapy.org/en/latest/)
* [Python 2.7](https://docs.python.org/2/library/index.html)

### Plung-in Environment
* Python2.7、setuptools、zope.interface
* Twisted、Scrapy
* lxml、BeautifulSoup4、win32py、pyOpenSSL

### How to start
* douban: the main program, use to run the crawler
```
//Scrapy crawl ItemName
  Scrapy crawl bookItem
  Scrapy crawl movieItem
```
* fetch_proxies: use to fetch the usalbe IP proxies
* This is designed to avoid the web forbid the crawler running
```
//finally catch the values in the file "proxies.json"
//then paste this into the douban/douban-setting.py instead of the contents of the PROXIES
  python fetch_free_proxies.py
```

### Problems
* If you can't run the crawler, please run the "fetch_free_proxies.py" at first
* How to voiding-getting-banned [document](http://doc.scrapy.org/en/master/topics/practices.html#avoiding-getting-banned), I have already use these ways


