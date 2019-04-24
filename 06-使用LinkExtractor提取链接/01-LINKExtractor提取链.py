"""
1. 使用selector ： 提取少量连接的时候   selector就够用了
2. 使用LinkExtractor： 大量且复杂的连接

"""""
                 # allow=(), deny=(),
                 # allow_domains=(), deny_domains=(), restrict_xpaths=(),
                 # tags=('a', 'area'), attrs=('href',), canonicalize=False,
                 # unique=True, process_value=None, deny_extensions=None, restrict_css=(),
                 # strip=True


# le = LinkExtractor(restrict_css = 'ul.pager li.next')
# links = le.extract_links(response)
