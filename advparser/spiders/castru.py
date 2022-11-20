import scrapy
from scrapy.http import HtmlResponse
from advparser.items import AdvparserItem
from scrapy.loader import ItemLoader


class CastruSpider(scrapy.Spider):
    name = 'castru'
    allowed_domains = ['castorama.ru']
    start_urls = ['https://www.castorama.ru/catalogsearch/result/?q=%D1%88%D0%BA%D0%B0%D1%84']

    # def __init__(self, name=None, **kwargs):
    #     super().__init__(name, **kwargs)
    #     self.start_urls = [f"https://leroymerlin.kz/search/?q={kwargs.get('query')}"]

    def parse(self, response):

        links = response.xpath('//a[@class="product-card__name ga-product-card-name"]')
        for link in links:
            yield response.follow(link, callback=self.item_parse)

    def item_parse(self, response: HtmlResponse):
        loader = ItemLoader(item=AdvparserItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('price', "//div[contains(@class, 'add-to-cart')]//span[@class='price']/span/span[1]/text()")
        loader.add_xpath('photos', "//img[contains(@class, 'top-slide__img')]/@data-src")
        loader.add_value('url', response.url)
        loader.add_xpath('attr_label', "//div[@id='specifications']//span[contains(@class, 'attribute-name')]/text()")
        loader.add_xpath('attr_value', "//div[@id='specifications']//dd/text()")
        yield loader.load_item()
