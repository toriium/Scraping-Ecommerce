from selenium import webdriver


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
        'hdd_128': price_hdd_128,
        'hdd_256': price_hdd_256,
        'hdd_512': price_hdd_512,
        'hdd_1024': price_hdd_1024,
    }
    nav.close()
    return prices
