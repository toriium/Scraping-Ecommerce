import time
from pprint import pprint

from playwright.sync_api import sync_playwright

from crawler_functions import get_only_numbers, remove_dollar_sign


class PlaywrightManager:
    __playwright = None
    __browser = None
    __page = None

    @classmethod
    def create_playwright_page(cls):
        cls.__playwright = sync_playwright().start()
        cls.__browser = cls.__playwright.chromium.launch(headless=False, slow_mo=50)
        cls.__page = cls.__browser.new_page()

    @classmethod
    def get_page(cls):
        if not cls.__page:
            cls.create_playwright_page()
        return cls.__page

    @classmethod
    def close_page(cls):
        cls.__browser.close()
        cls.__playwright.stop()


def laptops_link_generator(page, brand: str):
    links_list = []
    baseurl = 'https://webscraper.io'

    page.goto('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
    elements = page.query_selector_all('//div[@class="caption"]/h4[2]/a')
    for element in elements:
        if brand.upper() in element.get_attribute('title').upper():
            href = element.get_attribute('href')
            links_list.append(baseurl + str(href))
            # break
    return links_list


def crawler(brand: str):
    page = PlaywrightManager.get_page()
    laptops_links = laptops_link_generator(page=page, brand=brand)

    laptops_list = []
    for product in laptops_links:
        page.goto(product)

        id_laptop = get_only_numbers(product)
        name = page.query_selector_all('h4')[1].text_content()
        description = page.query_selector('[class="description"]').text_content()
        stars = len(page.query_selector_all('//div[@class="ratings"]/p/span'))
        reviews = get_only_numbers(page.query_selector('//div[@class="ratings"]/p').text_content())

        price128 = page.query_selector('[class="pull-right price"]').text_content()
        page.query_selector('[value="256"]').click()
        price256 = page.query_selector('[class="pull-right price"]').text_content()
        page.query_selector('[value="512"]').click()
        price512 = page.query_selector('[class="pull-right price"]').text_content()
        page.query_selector('[value="1024"]').click()
        price1024 = page.query_selector('[class="pull-right price"]').text_content()

        laptop = {
            'id_laptop': id_laptop,
            'name': name,
            'price_hdd_128': price128,
            'price_hdd_256': price256,
            'price_hdd_512': price512,
            'price_hdd_1024': price1024,
            'description': description,
            'reviews': reviews,
            'stars': stars
        }

        # print('saving: ', laptop['id_laptop']) # Terminal Log
        laptops_list.append(laptop)

    PlaywrightManager.close_page()
    pprint(laptops_list)


if __name__ == '__main__':
    crawler(brand='lenovo')
