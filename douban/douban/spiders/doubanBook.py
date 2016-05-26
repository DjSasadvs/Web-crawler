#coding=utf-8
import re
import json
import scrapy
import urllib
import sys

from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle

from douban.bookItems import BookItem

class BookSpider(scrapy.Spider):
    """docstring for BookSpider"""
    name = "book"
    allowed_domains = ["book.douban.com"]
    start_urls = [
        "https://book.douban.com/tag/",
    ]
    custom_settings = {
      'ITEM_PIPELINES':{'douban.pipelines.JsonWithEncodingBookPipeline': 400},
    }

    def start_requests(self):
          yield scrapy.Request("https://book.douban.com/subject/26264154/",
                        headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"})

    def parse(self, response):
        print "1"
        sel = Selector(response)
        sites = sel.css('#wrapper')
        for site in sites:
            item = BookItem()
            item['tittle'] = site.css('h1 span::text').extract()
            item['link'] = response.url
            # item['content_intro'] = site.css('#link-report .intro p::text').extract()
            item['rate'] = site.css('#interest_sectl .rating_self.clearfix strong::text').extract()
            item['author_intro'] = site.css('#info span:nth-child(1) a::text').extract()
            print item
            yield item

# rules = [
#     Rule(sle(allow=("/subject/\d+/?$")), callback='parse_book',),
#     Rule(sle(allow=("/tag/[^/]+/?$", )), follow=True, ),
#     Rule(sle(allow=("/tag/$", )), follow=True,),
# ]
        # next tag
        # tag = sel.css('//div[@id="tag"]/a/@href')
        tag = response.xpath('//div[@id="tag"]/a/@href')
        if tag:
          url = response.urljoin(tag[0].extract())
          yield scrapy.Request(url, self.parse, headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"})

        # next page
        page = response.xpath('//span[@id="thispage"]/a/@href')
        if page:
          url = response.urljoin(page[0].extract())
          yield scrapy.Request(url, self.parse, headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"})

        # next bookpage
        book_page = response.xpath('//li[@id="subject-item"]/div[@class="pic"]/a/@href')
        if book_page:
          url = response.urljoin(book_page[0].extract())
          yield scrapy.Request(url, self.parse, headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"})
