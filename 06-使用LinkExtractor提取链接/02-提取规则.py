from scrapy.http import HtmlResponse
html1 = open('example1.html', encoding='utf8').read()
html2 = open('example2.html', encoding='utf8').read()
# 创建两个response对象
re1 = HtmlResponse(url='http://example1.html', body=html1, encoding='utf8')
re2 = HtmlResponse(url='http://example2.html', body=html2, encoding='utf8')


# LinkExtractor参数解释
from scrapy.linkextractors import LinkExtractor

le = LinkExtractor()
links1 = le.extract_links(re1)
for link in links1:
    # url, text, fragment, nofollow
    print(link)




