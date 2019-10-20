from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'category')
    list_filter = ['category']
    search_fields = ['name_product']


admin.site.register(Category)
admin.site.register(Undercategory)
admin.site.register(Product, ProductAdmin)
