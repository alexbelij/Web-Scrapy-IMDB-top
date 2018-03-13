# -*- coding: utf-8 -*-
import scrapy
import urllib.parse as urlparse

from scrapy.loader.processors import TakeFirst, MapCompose, Compose
from scrapy.loader import ItemLoader
from IMDBTop.items import ImdbtopItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['imdb.com']
    start_urls = ['http://m.imdb.com/chart/top']


    def parse(self, response):
        urls = response.xpath('//*[@id="chart-content"]//a/@href').extract()

        for url in urls:
            yield scrapy.Request(urlparse.urljoin(response.url, url), callback=self.parse_item)

    def parse_item(self, response):
        def find_string(values):
            for value in values:
                # split out vote, we do not expect raw string here
                if r'/' not in value:
                    return value

        i = ItemLoader(item=ImdbtopItem(), response=response)
        i.add_xpath('title', '//*[@class="media-body"]//h1/text()', TakeFirst(), MapCompose(str.strip))
        i.add_xpath('year', '//*[@class="sub-header"]/text()', TakeFirst(), MapCompose(str.strip), re='\(([^)]+)\)')
        i.add_xpath('length', '//*[@itemprop="duration"]/text()', TakeFirst(), MapCompose(str.strip))
        i.add_xpath('rating', '//*[@itemprop="contentRating"]/@content', TakeFirst(), MapCompose(str.strip))
        i.add_xpath('genre', '//*[@itemprop="genre"]/text()')
        i.add_xpath('score', '//span[contains(@class, "inline-block") and contains(@class, "text-left") and contains(@class, "vertically-middle")]/text()', TakeFirst())
        i.add_xpath('vote', '//small[@class="text-muted"]/text()', Compose(find_string))

        yield i.load_item()


