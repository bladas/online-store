import json

from home.models import Category, UnderCategory, Product


def create(json, Category, UnderCategory, Product):
    with open('citrus.json', 'r') as json_file:
        data = json.load(json_file)

        for elem in data:
            print(elem.get('name'))
            print(elem.get('category'))
            print(elem.get('undercategory'))
            print(elem.get('price'))

            # new_category = Category.objects.create(title=elem.get('category'))
            # new_uc = UnderCategory.objects.create(title=elem.get('undercategory'), category=new_category)
            # new_product = Product.objects.create(name=elem.get('name'), ucategory=new_uc)
            # new_category.save()
            # new_uc.save()
            # new_product = Product.objects.create(name=elem.get('name'), ucategory=new_uc)

            try:
                category = Category.objects.get(title=elem.get('category'))
                try:
                   ucategory =  UnderCategory.objects.get(title=elem.get('undercategory'), category=category)
                   new_product = Product.objects.create(name=elem.get('name'), ucategory=ucategory,
                                                        price=elem.get('price'))
                   new_product.save()
                except:
                    new_uc = UnderCategory.objects.create(title=elem.get('undercategory'), category=new_category)
                    new_uc.save()
                    new_product = Product.objects.create(name=elem.get('name'), ucategory=new_uc,
                                                         price=elem.get('price'))
                    new_product.save()


            except:
                new_category = Category.objects.create(title=elem.get('category'))
                new_category.save()
                try:
                    print(UnderCategory.objects.get(title=elem.get('undercategory'), category=new_category))


                except:
                    new_uc = UnderCategory.objects.create(title=elem.get('undercategory'), category=new_category)
                    new_uc.save()
                    new_product = Product.objects.create(name=elem.get('name'), ucategory=new_uc,price=elem.get('price'))
                    new_product.save()




# print(create())
create(json, Category, UnderCategory, Product)
