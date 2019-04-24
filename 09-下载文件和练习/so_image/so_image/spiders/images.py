# -*- coding: utf-8 -*-
import scrapy
import json


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['image.so.com']
    BASE_URL = 'http://image.so.com/zj?ch=art&sn=%s&listtype=new&temp=1'
    start_index = 0
    # 限制最大数量   防止磁盘用的太多
    MAX_DOWNLOAD_NUM = 10
    start_urls = [BASE_URL % 0]

    def parse(self, response):
        infos = json.loads(response.body.decode('utf-8'))
        yield {'image_urls': [info['qhimg_url'] for info in infos['list']]}

        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield scrapy.Request(url=self.BASE_URL % self.start_index)


