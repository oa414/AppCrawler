# -*- coding: utf-8 -*-
import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from app.items import GoogleItem


class GoogleSpider(CrawlSpider):
    name = "google"
    allowed_domains = ["play.google.com"]
    start_urls = [
        'http://play.google.com/',
        'https://play.google.com/store/apps/details?id=com.viber.voip'
    ]
    rules = [
        Rule(LinkExtractor(allow=("https://play.google.com/store/apps/details", )), callback='parse_app',follow=True),
    ]

    
    def parse_app(self, response):
    	item = GoogleItem()
    	item['url'] = response.url
    	item['num'] =  response.xpath("//div[@itemprop='numDownloads']").xpath("text()").extract()
    	yield item
