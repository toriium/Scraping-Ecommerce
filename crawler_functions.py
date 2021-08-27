from selenium.webdriver import Chrome
import re


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


def get_prices(link):
    browser = Chrome()

    browser.get(link)

    price_element = browser.find_element_by_css_selector('[class="pull-right price"]')

    browser.find_element_by_css_selector('[value="128"]').click()
    price_hdd_128 = price_element.text

    browser.find_element_by_css_selector('[value="256"]').click()
    price_hdd_256 = price_element.text

    browser.find_element_by_css_selector('[value="512"]').click()
    price_hdd_512 = price_element.text

    browser.find_element_by_css_selector('[value="1024"]').click()
    price_hdd_1024 = price_element.text

    prices = {
        'hdd_128': remove_dollar_sign(price_hdd_128),
        'hdd_256': remove_dollar_sign(price_hdd_256),
        'hdd_512': remove_dollar_sign(price_hdd_512),
        'hdd_1024': remove_dollar_sign(price_hdd_1024),
    }
    browser.close()
    return prices
