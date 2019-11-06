import json
import urllib.request

from bs4 import BeautifulSoup


urls = {
    'https://rozetka.com.ua/tablets/c130309/filter/',
}
url1 = 'https://rozetka.com.ua/notebooks/c80004/filter/',


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


product = []


def parse(html):
    soup = BeautifulSoup(html)
    div = soup.find('div', class_='col-main container clearfix')
    for row in div.find_all('div', class_='g-i-tile g-i-tile-catalog'):
        cols = row.find_all('div', class_='g-i-tile-i-title clearfix')
        # print(div.h1.text)
        print(cols[0].a.text)
        product.append({
            # 'category': div.h1.text[1:1],
            'objects': [
                {
                    'object_name': cols[0].a.text[1:1]
                }
            ]

        })

    return product


def save(product):
    with open('product.json', 'w') as f:
        json.dump(product, f)


def main():
    parse(get_html(url1))
    save(product)


main()
