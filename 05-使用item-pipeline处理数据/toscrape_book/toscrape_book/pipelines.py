# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import pymongo
from scrapy.item import Item


class ToscrapeBookPipeline(object):
    def process_item(self, item, spider):
        return item


class BookPipeline(object):
    review_rating_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5
    }

    def process_item(self, item, spider):
        rating = item.get('review_rating')
        if rating:
            item['review_rating'] = self.review_rating_map[rating]

        return item


class DuplicatesPipelines(object):
    def __init__(self):
        self.book_set = set()       # 利用集合去重

    def process_item(self, item, spider):
        name = item['name']
        if name in self.book_set:
            raise DropItem('Duplicate  book found: %s ' % item)     # 依次添加进集合中，若存在就抛异常

        self.book_set.add(name)
        return item


class MongoDBPipeline(object):
    # 、mongodb的地址和名字
    DB_URL = 'mongodb://localhost:27017/'
    DB_NAME = 'scrapy_data'

    def open_spider(self, spider):
        # 打开mongodb
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]

    def closing_spider(self, spider):
        # 关闭mongodb
        self.client.close()

    def process_item(self, item, spider):
        #
        collection = self.db[spider.name]
        post = dict(item) if isinstance(item, Item) else item
        collection.insert_one(post)
        return item


# 对于mongodb配置文件形式实现
class MongoDBSETTINGPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        # 代替属性中的DB_URL,DB_NAME
        # cls: ITEM PIPeline类的对象
        # crawler： scrapy的核心对象， 只可以通过crawler.settings.get访问对象
        # 需要在setting中设置属性配置：MONGO_DB_URL = 'mongodb://localhost:27017/'
        #                           MONGO_DB_NAME = 'scrapy_data'
        cls.DB_URL = crawler.settings.get('MONGO_DB_URL', 'mongodb://localhost:27017/')
        cls.DB_NAME = crawler.settings.get('MONGO_DB_NAME', 'scrapy_data1')

        return cls()

    def open_spider(self, spider):
        # 打开mongodb
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]

    def closing_spider(self, spider):
        # 关闭mongodb
        self.client.close()

    def process_item(self, item, spider):
        #
        collection = self.db[spider.name]
        post = dict(item) if isinstance(item, Item) else item
        collection.insert_one(post)
        return item
