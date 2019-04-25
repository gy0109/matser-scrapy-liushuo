"""
1.OCR识别： 光学字符串  用于图片中图区文本信息  tesseract-ocr是利用该技术户实现的一个验证码识别库 pytesseract模块


"""""
from PIL import Image
import pytesseract

img = Image.open('./code1.png')
img = img.convert('L')
print(pytesseract.image_to_string(img))



"""
模拟登陆流程：
1. 初始化登录信息
2. 登录页面解析函数， 提取到输入用户名和密码的输入框，带入初始化信息，获取code图片，模拟登陆
3. 判断是否登录成功函数： 判断error信息
4. 解析code图片的函数: img.open(), img.conervt('L') pytesseract.image_to_string(img)  img.close() 文件打开要关闭的哦

"""