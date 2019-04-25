# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_splash import SplashRequest
import re

lua_script = """
function mian(splash)
    splash:go(splash.args.url)
    splash:wait(2)
    splash:runjs("document.getElementsByClassName('page')[0].scrollIntoView(true)")
    splash:wait(2)
    return splash:html()
"""


class JdBookSpider(scrapy.Spider):
    name = 'jd_book'
    allowed_domains = ['search.jd.com']
    base_url = 'https://search.jd.com/Search?keyword=python&enc=utf-8&wq=python'

    def parse_urls(self, response):
        # li.gl-item div.gl-i-wrap
        # 图片 div.p-img a-title img src---图片
        #   p-price i
        #  p-name  em font
        gross = response.css('span#J_resCount::text').extract_first()
        total = int(float(re.search('\d+\.\d+', gross).group()) * 100)
        pageNum = total//60 + (1 if total % 60 else 0)
        for i in range(pageNum):
            url = '%s&page=%s' % (self.base_url, 2*i +1)
            yield SplashRequest(url, endpoint='execute',
                                args={'lua_source': lua_script},
                                cache_args=['lua_source'], callback=self.parse)

    def start_requests(self):
        # 第一个页面不需要js渲染
        yield Request(self.base_url, callback=self.parse_urls, dont_filter=True)

    def parse(self, response):
        for sel in response.css('ul.gl-warp clearfix > li.gl.item'):
            re_dict = {
                'name': sel.css('div.p-name').xpath('string(.//em)').extract_fiest(),
                'price': sel.css('div.p-price i::text').extract_first()
            }
            yield Request(re_dict)
