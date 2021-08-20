import requests
from bs4 import BeautifulSoup
import re
from selenium_crawler import get_prices

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}


def get_only_numbers(text_received):
    regex_syntax = r"\D"
    num_str = re.sub(regex_syntax, "", text_received)
    num = int(num_str)

    return num


def laptops_link_generator():
    links_list = []
    baseurl = 'https://webscraper.io'

    r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')
    for item in productlist:
        for link in item.find_all('a', href=True):
            links_list.append(baseurl + link['href'])

    return links_list


def laptops_crawler():
    laptops_links = laptops_link_generator()

    laptops_list = []

    for link in laptops_links:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        id_laptop = get_only_numbers(link)
        name = soup.find('h4', class_='').text
        # price = soup.find('h4', class_='pull-right price').text
        description = soup.find('p', class_='description').text
        stars = len(soup.find_all('span', class_='glyphicon glyphicon-star'))
        prices = get_prices(link)

        find_reviews = soup.find_all('p', class_='')[4]
        for text in find_reviews:
            reviews = str(text.strip())
            break
        reviews = get_only_numbers(reviews)

        laptop = {
            'id_laptop': id_laptop,
            'name': name,
            'prices': prices,
            'description': description,
            'reviews': reviews,
            'stars': stars
        }

        print('saving: ', laptop['id_laptop'])
        laptops_list.append(laptop)

    return laptops_list
