import scrapy


class LaptopsSpider(scrapy.Spider):
    name = 'laptops'
    allowed_domains = ['webscraper.io']
    start_urls = ['https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops']

    def parse(self, response):
        for item in response.css('[class="thumbnail"]'):
            yield{
                'name': item.css('a.title::attr(title)').get(),
                'price': item.css('h4[class="pull-right price"]::text').get(),
                'description': item.css('p[class="description"]::text').get(),
                'stars': item.xpath('//div[@class="ratings"]/p[2]/@data-rating').get(),
                'reviwes': item.xpath('//div[@class="ratings"]/p[1]/text()').get()
            }
