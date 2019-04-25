"""
1.OCR识别： 光学字符串  用于图片中图区文本信息  tesseract-ocr是利用该技术户实现的一个验证码识别库 pytesseract模块


"""""
from PIL import Image
import pytesseract

img = Image.open('./code.png')
img = img.convert('L')
print(pytesseract.image_to_string(img))

