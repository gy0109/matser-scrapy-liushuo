# 爬取matplotlib所有子文件

# https://matplotlib.org/examples/index.html

# *********************************************************

from scrapy.pipelines.files import FilesPipeline

# 解决文件下载后  sha1编码的问题

class MyFilesPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        # path = urlparse(request.url).path   # 获当前的名称
        # return join(basename(dirname(path)), basename(path))   # 添加 到  修改
        pass


ITEM_PIPELINES = {
   'matplotlib_examples.pipelines.MyFilesPipeline': 1,      # 解决下载文件时文件名编码sha1问题
    # 'scrapy.pipelines.files.FilesPipeline': 1,       # 使用FilesPipeline
}
FILES_STORE = 'examples_src'         # 指定下载文件


# ***********************************************************