import json
from home.models import Category
from django.conf import settings

settings.configure(DEBUG=True)


def create():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        for elem in data:
            print(elem.get('title'))
            new_category = Category.objects.create(title=elem.get('title'))
            new_category.save()


create()
