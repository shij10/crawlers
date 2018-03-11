# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from example.items import ExampleItem

class FangSpider(CrawlSpider):
    name = 'fang'
    allowed_domains = ['esf.cd.fang.com']
    start_urls = ['http://esf.cd.fang.com/chengjiao/h37/']

    rules = (
        Rule(LinkExtractor(allow=r'chengjiao'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        connections = response.xpath('//dl[@id]')

        for connection in connections:
            item = ExampleItem()
            item['name'] = connection.xpath('dd/p[1]/a/text()').extract()[0].strip()
            item['total_price'] = connection.xpath('dd/div[3]/p[1]/span[1]/text()').extract()[0].strip()
            item['average_price'] = connection.xpath('dd/div[3]/p[2]/b/text()').extract()[0].strip()
            yield item

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

