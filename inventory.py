import requests
from bs4 import BeautifulSoup
import os

URLending = ['jackets', 'shirts', 'tops_sweaters', 'sweatshirts', 'pants', 't-shirts', 'hats', 'bags', 'accessories', 'skate']

file = open("supremeproducts.txt", 'w+')
for URLS in URLending:
    file.write(URLS.upper() + '\n\n\n')
    URL = 'https://www.supremenewyork.com/shop/all/' + URLS
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='container')

    products = results.find_all('li')
    for product in products:
        name = product.find_all(class_ = 'product-name')[0].text
        if name[-1]==' ':
            name = name[:-1]
        colour = product.find_all(class_ = 'product-style')[0].text
        soldout = product.find_all('a')[0].text
        link = 'https://www.supremenewyork.com' + product.find('a').get('href')
        a = name + ' ' + colour + ' - ' + soldout + ' ' + link
        file.write(a + '\n\n')
    file.write('\n\n')

file.close()





#product = results.find_all('ul', class_='inner_article')
#print(soup)
#print(results.prettify())
#print(products)