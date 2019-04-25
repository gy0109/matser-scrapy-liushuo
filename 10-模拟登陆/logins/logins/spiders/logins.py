import base64

import scrapy
import pytesseract
from PIL import Image
from io import BytesIO
from scrapy import Request
from scrapy.log import logger
import json


class CaptchalLoginSpider(scrapy.Spider):
    name = 'login_captcha'
    start_url = ['http://jdjffs.com']

    def parse(self, response):
        ...

    login_url = ''
    user_name = ''
    passward = ''

    def start_requests(self):
        yield Request(self.login_url, callback=self.login, dont_filter=True)    #

    def login(self, response):
        login_response = response.meta.get('login_response')

        if not login_response:
            cap1 = response.css().extract_first()
            cap1 = response.urljoin(cap1)
            yield Request(cap1, callback=self.login, meta={'login_response': response}, dont_filter=True)

        else:
            formdata = {
                'email': self.user_name,
                'passward': self.passward,
                'code': self.get_captcha_by_OCR(response.body),
            }

            yield Request(login_response, callback=self.login, formdata=formdata, dont_filter=True)

    def get_captcha_by_OCR(self, data):
        # OCR获取code的信息
        img = Image.open(BytesIO(data))
        img = img.convert('L')
        captcha = pytesseract.image_to_string(img)
        img.close()
        return captcha

    # 判断登录是否成功函数
    def parse_login(self, response):
        info = json.loads(response.text)
        if info['error'] == '0':
            logger.info('登录成功')
            return super().start_requests()

        logger.info('登录失败，请重新登录')
        return self.start_requests()

    def get_captcha_by_network(self, data):
        # 网络平台解析code
        import requests
        url = ''
        appcode = ''
        form = {}
        form['convert_to_jpg'] = '0'   #  是否将图片转换为jpg形式
        form['img_base64'] = base64.b64encode(data)       # 图片的数据形式转为64
        form['typeId'] =  '3040'         # 验证码类型，代表几位汉字

        headers = {}
        response = requests.post(url, headers=headers, data=form)
        res = response.json()

        if res['showapi_res_code'] == 0:
            return res['showapi_res_body']['Result']
        return ''

    def get_captcha_by_user(self, data):
        # 人工识别
        img = Image.open(BytesIO(data))
        img.show()
        captcha = input('请输入验证码：')
        # img = img.convert('L')
        # pytesseract.image_to_string(img)
        img.close()
        return captcha
