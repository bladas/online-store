import json


from home.models import Product,Category
from django.conf import settings

settings.configure(DEBUG=True)




def create():
    with open('product.json', 'r') as json_file:
        data = json.load(json_file)
        for elem in data:
            print(elem.get('title'))
            new_category = Product.objects.create(name_product=elem.get('title'),category_id= 0)
            new_category.save()


create()
