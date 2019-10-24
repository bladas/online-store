import json
from home.models import Undercategory
from django.conf import settings

settings.configure(DEBUG=True)
# my_model = apps.get_model('home', 'U')

def create():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        for elem in data:
            print(elem.get('title'))
            new_category = Undercategory.objects.create(title=elem.get('title'))
        # new_category = Undercategory(title=elem.get('title'))
            new_category.save()


create()
