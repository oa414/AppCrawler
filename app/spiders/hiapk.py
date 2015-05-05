# -*- coding: utf-8 -*-
import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from app.items import HiapkItem


class HiapkSpider(CrawlSpider):
    name = "hiapk"
    allowed_domains = ["hiapk.com"]
    start_urls = (
        'http://apk.hiapk.com/apps',
    )
    rules = [
        Rule(LinkExtractor(allow=("http://apk.hiapk.com/appinfo/", )), callback='parse_app',follow=True),
    ]



    def parse_app(self, response):
    	item = HiapkItem()
    	item['url'] = response.url
    	item['info'] =  response.css(".line_content > span").xpath("text()").extract()
    	item['apk_url'] = 'http://apk.hiapk.com' + response.css("#appInfoDownUrl").xpath("@href").extract()[0]
    	item['name'] = response.css("#appSoftName").xpath("text()").extract()[0]
    	yield item

   



  
