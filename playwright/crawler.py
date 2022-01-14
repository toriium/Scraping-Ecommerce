import time
import pprint

from playwright.sync_api import sync_playwright
from crawler_functions import get_only_numbers, remove_dollar_sign


def laptops_link_generator(page):
    links_list = []
    baseurl = 'https://webscraper.io'

    page.goto('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
    links = page.query_selector_all('//div[@class="caption"]/h4[2]/a')
    for link in links:
        href = link.get_attribute('href')
        links_list.append(baseurl + str(href))
        # break

    return links_list


def crawler():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()

    # pega cada um dos links dos laptops
    laptops_links = laptops_link_generator(page=page)

    # pega a infromação dos laptops
    laptops_list = []
    for product in laptops_links:
        page.goto(product)

        id_laptop = get_only_numbers(product)
        name = page.query_selector_all('h4')[1].text_content()
        price128 = page.query_selector('[class="pull-right price"]').text_content()
        page.query_selector('[value="256"]').click()
        price256 = page.query_selector('[class="pull-right price"]').text_content()
        page.query_selector('[value="512"]').click()
        price512 = page.query_selector('[class="pull-right price"]').text_content()

        laptop = {
            'id_laptop': id_laptop,
            'name': name,
            'price_hdd_128': price128,
            'price_hdd_256': price256,
            'price_hdd_512': price512,
        }

        # print('saving: ', laptop['id_laptop']) # Terminal Log
        laptops_list.append(laptop)

    browser.close()
    playwright.stop()
    pprint.pprint(laptops_list)


if __name__ == '__main__':
    crawler()
