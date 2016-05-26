#coding=utf-8
import scrapy
from douban.movieItems import MovieItem

class MovieSpider(scrapy.Spider):
  """docstring for MovieSpider"""
  name = 'movieItem'
  allowed_domains = ["douban.com"]
  # crawle need to pay at least 25$/m，so expensive
  # crawlera_enabled = True
  # crawlera_apikey = '<7b7bf3a2ae27425882b95b894b05ed3c>'
  start_urls = [
    "http://movie.douban.com/top250/"
  ]
  custom_settings = {
    'ITEM_PIPELINES':{'douban.pipelines.JsonWithEncodingMoviePipeline': 300},
  }

  def start_requests(self):
        yield scrapy.Request("http://movie.douban.com/top250/",
                      headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"})

  def parse(self, response):
    for content in response.xpath('//div[@class="item"]'):
      item = MovieItem()
      item['link'] = content.xpath('div[@class="pic"]/a/@href').extract()
      item['quote'] = content.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
      item['rate'] = content.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()
      item['rank'] = content.xpath('div[@class="pic"]/em/text()').extract()
      item['title'] = content.xpath('div[@class="pic"]/a/img/@alt').extract()
      yield item

    # next page
    page = response.xpath('//span[@class="next"]/a/@href')
    if page:
      url = response.urljoin(page[0].extract())
      yield scrapy.Request(url, self.parse, headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"})
