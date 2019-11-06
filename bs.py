import csv
import json
import time

from bs4 import BeautifulSoup
import requests

ROOT_URL = 'https://rozetka.com.ua'


def get_html(url):
    response = requests.get(url)
    # print(response.status_code)
    return response.content


def parse_url(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        container = soup.find('ul', class_='menu-categories menu-categories_type_main')
        for item in container.find_all('li', class_='menu-categories__item')[:-2]:
            temp_url = item.a.get('href')
            print("Category Url : " + temp_url)
            go_url(get_html(temp_url))
    except AttributeError:
        print("Restart Program Please (Internet so bad)")

    # except AttributeError:
    #     print("poymal except")


def go_url(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        container = soup.find('div', class_='custom-top-block portal-notebooks')
        for item in container.find_all('p', class_='h3 pab-h3'):
            temp_url_product = item.a.get('href')
            print("UC url: " + temp_url_product)
            parse(get_html(temp_url_product))
    except AttributeError:
        print("i cant get UC in Category")


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        # h1 = soup.find('div', class_='c-cols c-cols-inverse clearfix wrap')
        div = soup.find('div', class_='g-i-tile-l g-i-tile-catalog-hover-left-side clearfix')
        for row in div.find_all('div', class_='g-i-tile g-i-tile-catalog'):
            cols = row.find_all('div', class_='g-i-tile-i-title clearfix')
            print(cols[0].a.text)
    except AttributeError:
        # try:
        print("dont take product but we working")
        container = soup.find('div', class_='pab-table')
        for b in container.find_all('p', class_='pab-h4'):
            temp = b.a.get('href')
            parseproduct(get_html(temp))

    else:
        print("pizdec")


def parseproduct(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        h1 = soup.find('div', class_='c-cols c-cols-inverse clearfix wrap')
        div = soup.find('div', class_='g-i-tile-l g-i-tile-catalog-hover-left-side clearfix')
        for row in div.find_all('div', class_='g-i-tile g-i-tile-catalog'):
            cols = row.find_all('div', class_='g-i-tile-i-title clearfix')
            print(cols[0].a.text)
    except AttributeError:
        print("net shansov")


# def uc_category(html):
#     soup = BeautifulSoup(html, 'lxml')
#     try:
#         # h1 = soup.find('div', class_='c-cols c-cols-inverse clearfix wrap')
#         div = soup.find('div', class_='p-auto-block p-auto-block-1')
#         for row in div.find_all('div', class_='g-i-tile g-i-tile-catalog'):
#             cols = row.find_all('p', class_='pab-h4')
#             p
#             print(cols[0].a.text)
#     except:
#         print("dont take product")


#         product.append({
#             'category': h1.h1.text[1:-1],
#             'objects': [
#                 {
#                     'object_name': cols[0].a.text[1:-1]
#                 }
#             ]
#
#         })
#
#     return product


# def save(product):
#     with open('data.json', 'w') as f:
#         json.dump(product, f)


def main():
    parse_url(get_html(ROOT_URL))


if __name__ == '__main__':
    main()
