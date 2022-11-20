# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Compose, MapCompose, TakeFirst


def convert_price(value):
    value = value.replace('\xa0', '')
    try:
        value = int(value)
    except:
        return value
    return value


def parse_value(data):
    for num, elem in enumerate(data):
        elem = elem.strip()
        data[num] = elem
    return data


class AdvparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(convert_price), output_processor=TakeFirst())
    attr_label = scrapy.Field(input_processor=Compose(parse_value))
    attr_value = scrapy.Field(input_processor=Compose(parse_value))
    specifications = scrapy.Field()
    photos = scrapy.Field()
    _id = scrapy.Field()
