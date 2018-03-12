# coding=gbk

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import csv

class FangCrawlerPipeline(object):
    def __init__(self):
        self.file = codecs.open("results1.csv",'w','utf_8_sig')
        self.writer = csv.writer(self.file)

        self.writer.writerow(("名称","总价（万）","均价","成交日期","位置"))

    def process_item(self, item, spider):
        self.writer.writerow((item['name'], item['total_price'], item['average_price'], item['transaction_date'], item['location']))
        
        return item

    def __del__(self):
        self.file.close()
