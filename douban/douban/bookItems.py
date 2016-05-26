# -*- coding: utf-8 -*-

import scrapy
from scrapy.item import Item, Field

# This is about the bookItem fields
# # Declare book's fields

class BookItem(scrapy.Item):
    # id = Field()
    tittle = Field()
    link = Field()
    rate = Field()
    content_intro = Field()
    author_intro = Field()
