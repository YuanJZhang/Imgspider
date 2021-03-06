# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImgspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 图片地址
    imgurl = scrapy.Field()
    # 图片名称
    imgname = scrapy.Field()
    # 图片存放文件名
    dirname = scrapy.Field()

    pass
