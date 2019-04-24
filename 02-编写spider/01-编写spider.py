
"""
spider组件：

spider: 爬虫的入口 负责提取页面的数据， 并对新的页面进行下载请求
engine: 引擎， 框架的核心， 控制其他组件
downloader:  下载器， 下载页面
middleware: 中间件， 负责对request对象和response对象进行处理
item pipeline： 数据管道， 负责对爬取到的数据进行处理
scheduler:  调度器 负责对spider提交到饿下载请求进行调度

request: http请求对象
response: http响应对象
item: 从页面爬去一项数据

"""""


"""
框架执行顺序：

1. 当spider要爬取某url地址的页面时， 需要使用该url构造一个request对象  提交给engine
2. request对象随后进入scheduler按某种算法进行排队， 调度器在一定时间送他出队列，交给下载器
3， 下载器根据request对象中的url进行发送HTTP请求到网站的服务器， 之后服务器返回HTTP响应构造response对象  包含页面的html
4. response最终会被送给spider的页面解析函数 parse 页面解析函数从页面提取数据， 封装城item交给engine， 然后送入管道进行处理，最终可能有 exporter一某种数据格式写入文件，另一方面， 页面解析函数从页面提取url，构造新的request给引擎

"""


"""
request对象参数:
url,  method, headers,body,meta   ---常用
callback, cookies,  encoding, priority 优先级(默认为0 优先级高的请求优先)
dont_filter(False): 对一个url进行多次提交请求下载后面的请求会被去重，  True 请求避免过滤，强制性下载

"""





"""
response对象参数: 

url status, headers, boby, text, encoding,  request, meta, selector, 

常用参数：  
xpath, css, urljson(url) 构造绝对url，相对地址时  根据response.url构造绝对地址

"""


# 爬虫的步骤：  继承scrapy.Spider   name  start_url  def parse

# 定义爬虫的起点2种方法： start_url,
# def start_request:
#     yield scrapy.Request(url,
#                          callback=self.parse,
#                          headers='',
#                          dont_filter=True)