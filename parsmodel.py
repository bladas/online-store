from home.models import Undercategory


def create():
    Undercategory1 = open('data.json', 'r')
    for line in Undercategory1:
        new_category = Undercategory.objects.create(title= line)
        new_category.save()


if __name__ == '__main__':
    create()
