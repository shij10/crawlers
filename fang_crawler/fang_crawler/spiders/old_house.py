# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fang_crawler.items import FangCrawlerItem

class OldHouseSpider(CrawlSpider):
    name = "old_house"
    allowed_domains = ["esf.cd.fang.com"]
    start_urls = ['http://esf.cd.fang.com/chengjiao/h37/']

    rules = (
        Rule(LinkExtractor(allow=r'chengjiao/h37'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        url = response.url
        connections = response.xpath('//dl[@id]')

        for connection in connections:
            item = FangCrawlerItem()
            item['name'] = connection.xpath('dd/p[1]/a/text()').extract()[0].strip()
            item['total_price'] = connection.xpath('dd/div[3]/p[1]/span[1]/text()').extract()[0].strip()
            item['average_price'] = connection.xpath('dd/div[3]/p[2]/b/text()').extract()[0].strip()
            item['transaction_date'] = connection.xpath('dd/div[2]/p[1]/text()').extract()[0].strip()
            item['location'] = connection.xpath('dd/p[3]/a[1]/text()').extract()[0].strip()

            yield item


