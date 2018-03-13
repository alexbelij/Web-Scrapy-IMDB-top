# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbtopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    rating = scrapy.Field()
    score = scrapy.Field()
    length = scrapy.Field()
    genre = scrapy.Field()
    vote = scrapy.Field()


