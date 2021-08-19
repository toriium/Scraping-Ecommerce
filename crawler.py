import requests
from bs4 import BeautifulSoup

baseurl = 'https://webscraper.io'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

def laptops_crawler():
    laptops_links = []

    r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')
    for item in productlist:
        for link in item.find_all('a', href=True):
            laptops_links.append(baseurl + link['href'])

    laptops_list = []
    id_laptop = 1

    for link in laptops_links:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        name = soup.find('h4', class_='').text
        price = soup.find('h4', class_='pull-right price').text
        description = soup.find('p', class_='description').text
        stars = len(soup.find_all('span', class_='glyphicon glyphicon-star'))

        find_reviews = soup.find_all('p', class_='')[4]
        for text in find_reviews:
            reviewers = str(text.strip())
            break

        laptop = {
            'id_laptop': id_laptop,
            'name': name,
            'price': price,
            'description': description,
            'reviewers': reviewers,
            'stars': stars
        }

        # print('saving: ', laptop['id_laptop'])
        laptops_list.append(laptop)

        id_laptop += 1

    return laptops_list
