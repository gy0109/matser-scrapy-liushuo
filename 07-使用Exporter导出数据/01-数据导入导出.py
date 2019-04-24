
"""
scrapy支持的数据格式为： 
json:
csv:
xml:
pickle:
marshal:
json lines:

"""""

"""
导出数据方式： 
1.命令行参数：   scrapy crawl -o books -t json bookd.json    
                settings配置字典： FEED_EXPORTERS_BASE 默认配置中的     FEED_EXPORTERS用户配置文件中的 
                
                新的导出路径：   FEED_EXPORTERS = {'excel':'......}
                
                scrapy crawl books -o 'export_data/%(name)s/%(time)s.csv   名称+时间.csv
                
2. 配置文件： FEED_URL = ’export_data/%(name)s.data'    导出路径
            FEED_FORMAT = 'csv'    导出数据格式
            FEED_EXPORTERS_FIELDS = ['name', 'author', 'price']    导出数据包含的字段
            FEED_EXPORTERS_ = {‘excel':....)    用户自定义字典  添加新的导出数据时使用
            

"""