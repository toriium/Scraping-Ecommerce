import re
import time
import pprint


from playwright.sync_api import sync_playwright


def get_only_numbers(text_received):
    regex_syntax = r"\D"
    num_str = re.sub(regex_syntax, "", text_received)
    num = int(num_str)
    return num


def remove_dollar_sign(text: str):
    text = text.replace('$', '')
    try:
        num = float(text)
    except ValueError:
        num = 0
    return num


def crawler():
    baseurl = 'https://webscraper.io'

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()

        # pega cada um dos links dos laptops
        page.goto('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
        links = page.query_selector_all('[class="caption"]')
        laptops_links = []
        for link in links:
            href = link.query_selector_all('h4')[1].query_selector('a').get_attribute('href')
            laptops_links.append(baseurl + str(href))
            # break

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

            pprint.pprint(laptops_list)


if __name__ == '__main__':
    crawler()
