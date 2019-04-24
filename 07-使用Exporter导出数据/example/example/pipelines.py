# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ExamplePipeline(object):
    def process_item(self, item, spider):
        return item


# pipeline不需要继承什么基类，只需要实现特定的方法   open_spider   close_spider  process_item
# process_item是必须要有的   用来处理spider怕取到的数据    item: 爬取到的一项数据   spider 爬取的spider对象
class BookPipeline(object):
    # 汇率
    exchange_rate = 8.5309

    def process_item(self, item, spider):

        price = float(item['price'][1:])
        item['price'] = '￥%.2f'% price

        return item
