
import scrapy


class CaptchalLoginSpider(scrapy.Spider):
    name = 'zhihu'
    start_url = ['https://www.zhihu.com/signup?next=%2F']

    def parse(self, response):
        response.css('').extract_first()
        response.xpath().extract_first()

