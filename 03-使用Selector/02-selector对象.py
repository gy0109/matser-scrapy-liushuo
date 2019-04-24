# 创建selector对象

from scrapy.selector import Selector
from scrapy.http import HtmlResponse


text = '''
        <html lang="en">
        <body>
            <h1>Hello word</h1>
            <h1>Hello scrapy</h1>
            <h1>Hello python</h1>
            <b>hello scrapy selector</b>
        
            <ul>
                <li>c==</li>
                <li>python</li>
                <li>java</li>
            </ul>
        
        </body>
        </html>

'''

body = '''
        <html lang="en">
        <body>
            <h1>Hello word</h1>
            <h1>Hello scrapy</h1>
            <h1>Hello python</h1>
            <b>hello scrapy selector</b>
        
            <ul>
                <li>c==</li>
                <li>python</li>
                <li>java</li>
            </ul>
        
        </body>
        </html>

'''

text2 = '''

 <ul>
                <li>c== <b>价格： 99.00元</b></li>
                <li>python <b>价格： 98.00元</b></li>
                <li>java <b>价格： 89.00元</b></li>
            </ul>

'''

# 创建对象
selector1 = Selector(text=text)

response = HtmlResponse(url='http://www.example.com', body=body, encoding='utf8')
selector2 = Selector(response=response)

selector3 = Selector(text=text2)
# print(selector1)
# print('*' * 10)
# print(selector2)

# 选中数据
selector1_list = selector1.xpath('.//h1')

for sel in selector1_list:
    print(sel.xpath('./text()').extract())
# print(selector1_list)

sel2 = selector1.xpath('.//ul').css('li').xpath('./text()')
print(sel2)


# 提取数据
s1 = selector1.xpath('.//li')    # 返回li的列表
print(s1[1].extract())                # extract返回选中内容的unicode字符串

s2 = selector1.xpath('.//li/text()')   #
print(s2.extract())

s3 = selector1.xpath('.//b')
print(s3.extract_first())             # 返回selector对象生成的extract结果

s4 = selector3.xpath('.//li/b/text()')
print(s4.extract())     # b标签下数据
print(s4.re(r'\d+\.\d+'))    # 提取金额整数
print(s4.re_first(r'\d+\.\d+'))    # 提取金额整数  的  第一个数据



# 简介的取数据方法

print(response.xpath('.//h1/text()').extract())
print(response.css('li::text').extract())

