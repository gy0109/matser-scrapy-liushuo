import re

from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor

html1 = open('example1.html', encoding='utf8').read()
html2 = open('example2.html', encoding='utf8').read()
# 创建两个response对象
re1 = HtmlResponse(url='http://example1.html', body=html1, encoding='utf8')
re2 = HtmlResponse(url='http://example2.html', body=html2, encoding='utf8')


def process(value):
    #   <a href="/intro/tutorial334----img.html">图片</a>
    # '/intro/.+\.html$'
    m = re.search(r'/intro/.+\.html$', value)
    if m:
        value = m.group(1)
    return value


# 接收一个func作为回调函数。 如果传递了该参数， Linkextractor将调用该回调函数对提取的每一个连接进行处理，  回调函数正常情况下应返回一个字符串，想要抛弃链接时会返回None
le = LinkExtractor(process_value=process)

links1 = le.extract_links(re2)
for link in links1:
    # url, text, fragment, nofollow
    print(link.url)



