"""
browerCookie可以获取Chrome和Firefox的cookie

import


"""""

import browsercookie
chrome_cookiejar = browsercookie.chrome()
# firefox_cookiejar = browsercookie.firefox()

print(type(chrome_cookiejar))

for i in chrome_cookiejar:
    print(i)


"""
源码分析：
from_crawler(): 从配置文件中读取cookies_enabled， 决定是否启用该中间件，如果启用调用构造器创建对象，，否则抛出异常
__init__: collections.defaultdict创建一个默认的字典self.jars




"""
