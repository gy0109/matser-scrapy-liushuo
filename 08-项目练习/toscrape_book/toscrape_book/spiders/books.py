import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem

class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/']
    allowed_domains = ['books.toscrape.com']

    # 书籍列表相关
    def parse(self, response):
        le = LinkExtractor(restrict_css='article.product_pod h3')       # 提取链接
        for link in le.extract_links(response):
            yield scrapy.Request(url=link.url, callback=self.parse_book)

        # 提取下一页内容
        le = LinkExtractor(restrict_css='ul.pager li.next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(url=next_url, callback=self.parse)

    # 书籍页面信息解析
    def parse_book(self, response):
        book = BookItem()
        sel = response.css('div.product_main')
        book['name'] = sel.xpath('./h1/text()').extract_first()
        book['price'] = sel.css('p.price_color::text').extract_first()
        book['review_rating'] = sel.css('p.star-rating::attr(class)').re_first(r'star-rating([A-Za-z]+)')

        sel = response.css('table.table.table-striped')
        book['review_num'] = sel.xpath('(.//tr)[last()]/td/text()').extract_first()
        # .table-striped > tbody > tr:nth-child(odd) > td, .table-striped > tbody > tr:nth-child(odd) > th
        book['upc'] = sel.xpath('(.//tr)[1]/td/text()').extract_first()
        # book['upc'] = sel.xpath('tbody/tr:nth-child(odd)/td/text()').extract_first()
        # .table > tbody > tr > th,
        # book['stock'] = sel.xpath('.//tr/td/text()').extract_first()
        book['stock'] = sel.xpath('(.//tr)[last()-1]/td/text()').re_first(r'\((\d+)available\)')

        yield book






