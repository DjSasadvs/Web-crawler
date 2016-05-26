# -*- coding: utf-8 -*-

import scrapy
from scrapy.item import Item, Field

# This is about the movieItem fields

class MovieItem(scrapy.Item):
    rank = Field()
    title = Field()
    link = Field()
    rate = Field()
    quote = Field()
