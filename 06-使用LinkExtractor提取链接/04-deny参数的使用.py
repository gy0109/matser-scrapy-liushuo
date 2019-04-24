from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse


html1 = open('example1.html', encoding='utf8').read()
html2 = open('example2.html', encoding='utf8').read()
# 创建两个response对象
re1 = HtmlResponse(url='http://example1.html', body=html1, encoding='utf8')
re2 = HtmlResponse(url='http://example2.html', body=html2, encoding='utf8')

# deny参数接收正则表达式或者正则表达式列表  与allow相反  排除绝对url和正则表达式匹配出来的数据
pattern = '^' + urlparse(re1.url).geturl()
le = LinkExtractor(deny=pattern)

links1 = le.extract_links(re1)
for link in links1:
    # url, text, fragment, nofollow
    print(link.url)




