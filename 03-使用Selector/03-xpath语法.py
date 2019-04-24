"""
xml文档的节点：   
根节点   元素节点   属性节点  文本节点
父子  兄弟  祖先 后裔 

"""""

"""
基础语法：
/： 一个从根开始的绝对路径
a/b: 原定a标签下面的b标签
a//b: a后代节点中所有b      ---- 后代
. ：当前节点    相对路径 
.. ：当前节点的父节点   绝对路经 
//标签 ：选中标签下的所有文档
标签 ：
  
*：所有元素子节点
*/a ： 所有孙节点中的 a
text()：  文本子节点
@属性：选中属性
//@属性：  文档中所有的某个属性
@*：
node[](查找某个特定节点或者包含某个特定值的节点)   [@id]  [@id='']


常用函数：

string(arg): 返回参数的字符串值   sel.xpath('.//h1/text()')== sel.xpath(string('.//h1'))
contains(str1, str2): 判断1中是否包含2返回布尔值  sel.xpath('//p[contains(@class, 'small')]')

"""


"""
CSS选择器： 
* ：所有玄素
E: 选中E元素
E1, E2: 选中E1， E2元素
E1 E2: 选中E1后代中的E2元素
E1>E2: 选中E1子元素中的E2元素
E1+E2: 选中E1兄弟元素的E2元素
.class: class属性中包含 class的元素
#id: id中包含某个id的元素
[attr]: 包含attr属性的元素
[attr=value]: 包含attr属性 并且值为value的元素
[attr~=value]: 包含attr属性 并且值包含value的元素



"""
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

body = '''
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <title>example website</title>
</head>
<body>
    <div id="image-1" style="width: 1230px;">
        <a href="image1.html">Name: Image 1<br><img src="image1.png"></a>
        <a href="image2.html">Name: Image 2<br><img src="image2.png"></a>
        <a href="image3.html">Name: Image 3<br><img src="image3.png"></a>
        <a href="image4.html">Name: Image 4<br><img src="image4.png"></a>
    </div>

<div id="image-2" style="width: 1230px;">   
    <a href="image4.html">Name: Image 4<br><img src="image4.png"></a>
    <a href="image5.html">Name: Image 4<br><img src="image5.png"></a>


</div>
</body>
</html>


'''
response = HtmlResponse(url='http:www.example.com', body=body, encoding='utf8')
print(response.css('img'))
print(response.css('base, title'))
print(response.css('div img'))
print(response.css('body>div'))
print(response.css('[style]'))
print(response.css('[id=image-1]'))
print(response.css('div>a:nth-child(1)'))
print(response.css('div:nth-child(2)>a:nth-child(1)'))
print(response.css('div:first-child>a:last-child'))
print(response.css('a::text'))


