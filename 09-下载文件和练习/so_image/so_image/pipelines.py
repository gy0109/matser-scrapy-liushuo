# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from os.path import dirname, basename, join
from urllib.parse import urlparse
# 解决文件下载后  sha1编码的问题


class SoImagePipeline(object):
    def process_item(self, item, spider):
        return item


class MyImagesPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        path = urlparse(request.url).path   # 获当前的名称
        return join(basename(dirname(path)))   # 添加 到  修改

