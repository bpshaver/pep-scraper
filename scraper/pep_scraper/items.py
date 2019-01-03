# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class PepScraperItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # From the first page:
    short_typ = Field()
    short_num = Field()
    short_tit = Field()
    short_aut = Field()
    url = Field(defualt='')

    # From the second page:
    PEP = Field()
    Title = Field()
    Author = Field()
    Status = Field()
    Type = Field()
    Created = Field()
    Post_History = Field()
    Python_Version = Field()
