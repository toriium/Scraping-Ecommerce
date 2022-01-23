import scrapy


class LaptopsSpider(scrapy.Spider):
    name = 'laptops'
    allowed_domains = ['https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops']
    start_urls = ['http://https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops/']

    def parse(self, response):
        pass
