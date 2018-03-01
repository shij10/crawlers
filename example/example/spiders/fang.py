# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FangSpider(CrawlSpider):
    name = 'fang'
    allowed_domains = ['esf.cd.fang.com']
    start_urls = ['http://esf.cd.fang.com/chengjiao/h37/']

    rules = (
        Rule(LinkExtractor(allow=r'chengjiao'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        url = response.url
        #titles = response.xpath('//dl/dd/p[1]/a/text()').extract()

        items = response.xpath('//dl')

        for index, item in enumerate(items):
            name = item.xpath('dd/p[1]/a/text()').extract()
            print(name)

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

