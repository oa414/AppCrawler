# -*- coding: utf-8 -*-
import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from app.items import AppItem

class BaiduSpider(CrawlSpider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://shouji.baidu.com/',
    )
    rules = [
        Rule(LinkExtractor(allow=("http://shouji.baidu.com/soft/item", )), callback='parse_app',follow=True),
    ]


    def parse_app(self, response):
    	apk = AppItem()
        apk['url']  = response.url
        apk['name'] = response.css('.app-name>span').extract()[0]
        apk['rate'] = response.css(".star-percent").xpath("@style").extract()[0]
        apk['size'] = response.css(".detail > span.size").xpath("text()").extract()[0]
        apk['category'] = response.css(".nav").css("a")[1].xpath("text()").extract()[0]
        apk['apk_url']  = response.css(".apk").xpath("@href").extract()[0]
        apk['screenshots']  = response.css(".imagefix").xpath("@src").extract()
        apk['download_num'] = response.css("span.download-num").xpath("text()").extract()[0]
    	yield apk
