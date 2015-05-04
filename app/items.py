# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppItem(scrapy.Item):
    apk_url  = scrapy.Field()
    name     = scrapy.Field()
    rate     = scrapy.Field()
    category = scrapy.Field()
    size     = scrapy.Field()
    url      = scrapy.Field()
    screenshots  = scrapy.Field()
    download_num = scrapy.Field()


class GoogleItem(scrapy.Item):
 	url = scrapy.Field()
 	num = scrapy.Field()