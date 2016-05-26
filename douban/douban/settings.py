# -*- coding: utf-8 -*-

# Scrapy settings for douban project
# Declare the filed and configurations here

BOT_NAME = 'douban'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'

DOWNLOAD_DELAY = 3

COOKIES_ENABLED = False

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
 ]

PROXIES = [
    {'ip_port': '111.126.229.52:8118', 'user_pass': ''},
    {'ip_port': '122.235.235.204:8188', 'user_pass': ''},
    {'ip_port': '43.226.162.107:80', 'user_pass': ''},
    {'ip_port': '106.2.120.174:80', 'user_pass': ''},
    {'ip_port': '106.2.99.224:80', 'user_pass': ''},
]

FEED_URI = u'file:///D:/python/douban/books.csv'
FEED_FORMAT = 'CSV'
#
# DEFAULT_REQUEST_HEADERS = {
#   # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#   # 'Accept-Language': 'zh-CN,zh;q=0.8',
#   'X-Crawlera-Cookies': 'disable'
# }

# CRAWLERA_ENABLED = True
# CRAWLERA_APIKEY = '<7b7bf3a2ae27425882b95b894b05ed3c>'

# CRAWLERA_PRESERVE_DELAY = True
# CONCURRENT_REQUESTS = 32
# CONCURRENT_REQUESTS_PER_DOMAIN = 32
# AUTOTHROTTLE_ENABLED = False
# DOWNLOAD_TIMEOUT = 600

DOWNLOADER_MIDDLEWARES = {
    # 'scrapy_crawlera.CrawleraMiddleware': 600
    'douban.middlewares.RandomUserAgent': 1,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'douban.middlewares.ProxyMiddleware': 100
}

ITEM_PIPELINES = {
    'douban.pipelines.JsonWithEncodingMoviePipeline': 200,
    'douban.pipelines.JsonWithEncodingBookPipeline': 300,
    # 'douban.pipelines.DuplicatesPipeline': 180,
    #'template.pipelines.RedisPipeline': 301,
}
