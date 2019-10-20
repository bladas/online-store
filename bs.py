import csv
import json

from bs4 import BeautifulSoup
import urllib.request


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


categories = []


def parse(html):
    soup = BeautifulSoup(html)
    div = soup.find('div', class_='container')
    for row in div.find_all('div', class_='pab-cell pab-img-150'):
        cols = row.find_all('p')
        categories.append({
            'title': cols[0].a.text[1:-1]
        })

    # for category in categories:
    #     print(category.get('title'))

    return categories


def save(categories):
    with open('data.json', 'w') as f:
        json.dump(categories, f)




def main():
    parse(get_html('https://rozetka.com.ua/computers-notebooks/c80253/'))
    save(categories)


if __name__ == '__main__':
    main()
