import json

from bs4 import BeautifulSoup
import urllib.request

url1 = 'https://rozetka.com.ua/notebooks/c80004/filter/'


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


product = []


def parse(html):
    soup = BeautifulSoup(html)
    div = soup.find('div', class_='cat-g-b clearfix')
    for row in div.find_all('div', class_='g-i-tile-i-box-desc'):
        cols = row.find_all('div', class_ = 'g-i-tile-i-title clearfix')
        product.append({
            'title': cols[0].a.text[1:-1]
        })



    return product


def save(product):
    with open('product.json', 'w') as f:
        json.dump(product, f)


def main():
    parse(get_html(url1))
    save(product)


main()
