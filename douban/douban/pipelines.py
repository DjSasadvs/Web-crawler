# -*- coding: utf-8 -*-

from scrapy import signals

import json
import codecs
from collections import OrderedDict

# This is about the Pipelines
# Use this to store the data with json sequence
# Includes douban_movie.json, douban_book.json

class JsonWithEncodingMoviePipeline(object):

    def __init__(self):
        self.file = codecs.open('douban_movie.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False, sort_keys=True) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class JsonWithEncodingBookPipeline(object):

    def __init__(self):
        self.file = codecs.open('douban_book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False, sort_keys=True) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class DuplicatesPipeline(object):

    def __init__(self):
        self.books_list = set()

    def process_item(self, item, spider):
        if item['tittle'] in self.books_list:
            raise DropItem("Duplicate books exit: %s" % item['tittle'])
        else:
            self.books_list.add(item['tittle'])
            return item
