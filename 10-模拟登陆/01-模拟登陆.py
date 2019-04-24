""""
页面表单：对应的form表单中提供登陆所需要的参数

form:  method提供请求方法
  action: 请求的url
  enctype: 表单数据的编码类型
  input： 获取输入的内容
  _fromkey: 防止csrf跨站伪造请求
  
  
"""""
# **********************************************************
# 模拟登陆
from scrapy.http import FormRequest

fd = {'email':'g17600550662@163.com', 'password':'gy980109'}

# request = FormRequest.from_response(response, formdata=fd)

# 'Welcomey' in response.text   #   测试是否成功登陆


# ************************************************************
# 提取页面个人信息