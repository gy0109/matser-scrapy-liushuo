from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor

html1 = open('example1.html', encoding='utf8').read()
html2 = open('example2.html', encoding='utf8').read()
# 创建两个response对象
re1 = HtmlResponse(url='http://example1.html', body=html1, encoding='utf8')
re2 = HtmlResponse(url='http://example2.html', body=html2, encoding='utf8')


# allow_dpmain参数接收一个域名或者域名列名， 提取指定域名
domains = ['github.com', 'lagou.com']
le = LinkExtractor(allow_domains=domains)

links1 = le.extract_links(re1)
for link in links1:
    # url, text, fragment, nofollow
    print(link.url)






