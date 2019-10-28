import json

from bs4 import BeautifulSoup
import urllib.request

url1 = 'https://rozetka.com.ua/computers-notebooks/c80253/'


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


product = []


def parse(html):
    soup = BeautifulSoup(html)
    div = soup.find('div', class_='container')
    for row in div.find_all('div', class_='pab-cell pab-img-150'):
        cols = row.find_all('p')
        product.append({
            'title': cols[0].a.text[1:-1]
        })

    # for category in categories:
    #     print(category.get('title'))

    return product


def save(product):
    with open('product.json', 'w') as f:
        json.dump(product, f)


def main():
    parse(get_html(url1))
    save(product)


main()
