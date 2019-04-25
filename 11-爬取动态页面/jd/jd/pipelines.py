# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class JdPipeline(object):
    def process_item(self, item, spider):
        return item


class JDPipeline(object):
    def __init__(self):
        self.book_set = set()

    def process_item(self, item, spider):
        name = item['name']
        # price = item['price']
        if name in self.book_set:
            raise DropItem('重复删除%s' % item)

        self.book_set.add(name)

        return item
