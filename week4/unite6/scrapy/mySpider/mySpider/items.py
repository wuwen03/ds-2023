# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DangdangItem(scrapy.Item):
    name=scrapy.Field()
    auther=scrapy.Field()
    price=scrapy.Field()
