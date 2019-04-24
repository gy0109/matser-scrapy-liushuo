

import scrapy


class BooksSpider(scrapy.Spider):
    # 每一个爬虫的唯一标识   一个spider可能有多个爬虫  所以那么是分辨每一个爬虫的唯一标识
    name = 'books'

    # 起始的url
    start_url = ['http://books.tocrape.com']

    # parse方法当一个页面下载之后  scrapy引擎会回调一个我们制定的页面回调函数 来解析页面
    # 两个任务： 解析页面的数据   xpath或css选择器    提取页面的连接  并对新的连接产生新的请求
    def parse(self, response):

        # css选择器   选择 每个图片下面的总位置
        for book in response.css('article.product_pod'):
            # book_name  在 article.product_pod下面的 h3>a>title   @title取title属性值
            name = book.xpath('./h3/a/@title').extract_first()
            # price 在article.product_pod下面的 p--class='price_color’  ：：text取标签内的值
            price = book.css('p.price_color::text').extract_first()
            yield {
                'name': name,
                'price': price
            }

        # 提取 下一页 链接  
        next_url = response.css('ul.pager li.next a::attr(href)').extrace_first()

        if next_url:
            next_url = response.urljson(next_url)
            yield scrapy.Request(next_url, callback=self.parse)


