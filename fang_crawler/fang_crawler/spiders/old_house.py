# -*- coding: utf-8 -*-
import scrapy
from fang_crawler.items import FangCrawlerItem

class OldHouseSpider(scrapy.Spider):
    name = "old_house"
    allowed_domains = ["esf.cd.fang.com/chengjiao/h37"]
    start_urls = ['http://esf.cd.fang.com/chengjiao/h37/']

    def parse(self, response):
        connections = response.xpath('//dl[@id]')

        for connection in connections:
            item = FangCrawlerItem()
            item['name'] = connection.xpath('dd/p[1]/a/text()').extract()[0].strip()
            item['total_price'] = connection.xpath('dd/div[3]/p[1]/span[1]/text()').extract()[0].strip()
            item['average_price'] = connection.xpath('dd/div[3]/p[2]/b/text()').extract()[0].strip()
            yield item

        pass
