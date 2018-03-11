# -*- coding: utf-8 -*-
import scrapy


class OldHouseSpider(scrapy.Spider):
    name = "old_house"
    allowed_domains = ["esf.cd.fang.com/chengjiao/h37/"]
    start_urls = ['http://esf.cd.fang.com/chengjiao/h37//']

    def parse(self, response):
        pass
