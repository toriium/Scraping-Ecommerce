import scrapy
from scrapy_bot.items import LaptopsSpiderItem
from scrapy.loader import ItemLoader


class LaptopsSpider(scrapy.Spider):
    name = 'laptops'
    allowed_domains = ['webscraper.io']
    start_urls = ['https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops']

    def parse(self, response):
        for product in response.css('[class="thumbnail"]'):
            i = ItemLoader(item=LaptopsSpiderItem(), selector=product)

            i.add_css('name', 'a.title::attr(title)')
            i.add_css('price', 'h4[class="pull-right price"]::text')
            i.add_css('description', 'p[class="description"]::text')
            i.add_xpath('stars', '//div[@class="ratings"]/p[2]/@data-rating')
            i.add_xpath('reviwes', '//div[@class="ratings"]/p[1]/text()')

            yield i.load_item()
