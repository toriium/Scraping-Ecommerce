# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class LaptopsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    description = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    stars = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    reviwes = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
