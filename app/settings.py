# -*- coding: utf-8 -*-

# Scrapy settings for app project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'app'

SPIDER_MODULES = ['app.spiders']
NEWSPIDER_MODULE = 'app.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'app (+http://www.yourdomain.com)'

ITEM_PIPELINES = [
  'scrapy_mongodb.MongoDBPipeline',
]

MONGODB_URI = 'mongodb://127.0.0.1:27017'
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'hiapk'

EXTENSIONS = {'scrapy.contrib.feedexport.FeedExporter': None}
