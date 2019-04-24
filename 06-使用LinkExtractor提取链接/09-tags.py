from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor

html1 = open('example1.html', encoding='utf8').read()
html2 = open('example2.html', encoding='utf8').read()
# 创建两个response对象
re1 = HtmlResponse(url='http://example1.html', body=html1, encoding='utf8')
re2 = HtmlResponse(url='http://example2.html', body=html2, encoding='utf8')


# 接收一个标签或者标签列表  取出符合条件的标签下的所有链接
le = LinkExtractor(tags='a', attrs='href')

links1 = le.extract_links(re2)
for link in links1:
    # url, text, fragment, nofollow
    print(link.url)












