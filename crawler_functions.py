from selenium import webdriver
import re


def get_only_numbers(text_received):
    regex_syntax = r"\D"
    num_str = re.sub(regex_syntax, "", text_received)
    num = int(num_str)
    return num


def remove_dollar_sign(text: str):
    text = text.replace('$', '')
    num = float(text)
    return num


def get_prices(link):
    nav = webdriver.Chrome()

    nav.get(link)

    nav.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[2]/button[1]").click()
    price_hdd_128 = nav.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]').text

    nav.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[2]/button[2]').click()
    price_hdd_256 = nav.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]').text

    nav.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[2]/button[3]').click()
    price_hdd_512 = nav.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]').text

    nav.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[2]/button[4]').click()
    price_hdd_1024 = nav.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]').text

    prices = {
        'hdd_128': remove_dollar_sign(price_hdd_128),
        'hdd_256': remove_dollar_sign(price_hdd_256),
        'hdd_512': remove_dollar_sign(price_hdd_512),
        'hdd_1024': remove_dollar_sign(price_hdd_1024),
    }
    nav.close()
    return prices
