#coding=utf-8
import re
import json
import scrapy


from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle

from douban.bookItems import BookItem

class BookSpider(CrawlSpider):
    """docstring for BookSpider"""
    name = "bookItem"
    # crawle need to pay at least 25$/m，so expensive
    # crawlera_enabled = True
    # crawlera_apikey = '<7b7bf3a2ae27425882b95b894b05ed3c>'
    allowed_domains = ["book.douban.com"]
    start_urls = [
        "https://book.douban.com/tag/",
        "https://book.douban.com/tag/%E5%A4%96%E5%9B%BD%E6%96%87%E5%AD%A6",
    ]
    custom_settings = {
      'ITEM_PIPELINES':{'douban.pipelines.JsonWithEncodingBookPipeline': 400},

    }
    rules = [
        Rule(sle(allow=("/subject/\d+/?$")), callback='parse_book',),
        Rule(sle(allow=("/tag/[^/]+/?$", )), follow=True, ),
        Rule(sle(allow=("/tag/$", )), follow=True,),
    ]

    # def add_cookies(self, request):
    #     request.replace(cookies=[
    #         {'name': 'COOKIE_NAME','value': 'VALUE','domain': '.douban.com','path': '/'},],
    #         headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
    #                 'referer':'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'}
    #         );
    #     return request;


    def start_requests(self):
          yield scrapy.Request("https://book.douban.com/tag/%E5%A4%96%E5%9B%BD%E6%96%87%E5%AD%A6",
                        headers={'X-Crawlera-Max-Retries': 1,'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"})

    def parse_book(self, response):
        items = []
        sel = Selector(response)
        sites = sel.css('#wrapper')
        for site in sites:
            item = BookItem()
            # wrapper > h1 > span
            item['tittle'] = site.css('h1 span::text').extract()
            item['link'] = response.url
            # link-report > span.all.hidden > div > div > p:nth-child(1)
            item['content_intro'] = site.css('#link-report .intro p::text').extract()
            # interest_sectl > div > div.rating_self.clearfix > strong
            item['rate'] = site.css('#interest_sectl .rating_self.clearfix strong::text').extract()
            # info > span:nth-child(1) > a
            item['author_intro'] = site.css('#info span:nth-child(1) a::text').extract()
            items.append(item)
            # print repr(item).decode("unicode-escape") + '\n'
            print item
            #print repr(item).decode("unicode-escape") + '\n'
        return items

        def _process_request(self, request):
            return request
