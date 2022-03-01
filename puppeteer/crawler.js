import puppeteer from 'puppeteer'

async function crawler() {
    const browser = await puppeteer.launch({ headless: false });

    const page = await browser.newPage();
    await page.goto('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops');
    let products_list
    let products = []

    products_list = await page.$x('//div[@class="thumbnail"]')
    console.log(`tamanho: ${products_list.length}`)

    for (let element of products_list) {
        // console.log('--------------------------------------');
        const name = await page.evaluate((element) => element.querySelector('a').getAttribute('title'), element); 
        const price = await page.evaluate((element) => element.querySelector('h4:nth-child(1)').textContent, element); 
        const description = await page.evaluate((element) => element.querySelector('p[class="description"]').textContent, element); 
        const reviews = await page.evaluate((element) => element.querySelector('div[class="ratings"] > p[class="pull-right"]').textContent, element); 
        const stars = await page.evaluate((element) => element.querySelector('div[class="ratings"] > p[data-rating]').getAttribute('data-rating'), element); 
        // console.log(valor)

        let laptop = {
            name: name,
            price: price,
            description: description,
            reviews: reviews,
            stars: stars,
        }
        products.push(laptop)
    }

    console.log(products)

    await browser.close();
};

crawler()