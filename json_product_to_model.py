import json

from home.models import Product, Category
from django.conf import settings

settings.configure(DEBUG=True)


def create():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        for elem in data:
            print(elem.get('category'))
            print(elem['objects']('object_name'))
            # new_category = Product.objects.create(name_product=elem.objects.get('object_name'))
            # new_category.save()


create()
