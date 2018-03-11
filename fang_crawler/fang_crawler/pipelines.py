# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import csv

class FangCrawlerPipeline(object):
    def process_item(self, item, spider):
        #with codecs.open("example.csv",'a+','utf-8') as f:

        #    writer = csv.writer(f)
        #    writer.writerow((item['name'].decode('gbk'), item['total_price'], item['average_price']))
        return item
