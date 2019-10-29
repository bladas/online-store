from datetime import datetime
from django.db import models
from model_utils import Choices
from enum import Enum


# class Category(models.Model):
#     CATEGORY_CHOICES = Choices('Ноутбуки и компьютеры', 'Бытовая техника', 'Смартфоны, ТВ и электроника',
#                                'Товары для дома', 'Инструменты и автотовары', 'Сантехника и ремонт',
#                                'Дача, сад и огорд', 'Спорт и увлечения', 'Одежда, обувь и уркашения',
#                                'Красота и здоровье', 'Детские товары', 'Канцтовары и книги',
#                                'Алкогольные напитки и продукты', 'Товары для бизнеса')
#     title = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Ноутбуки и компьютеры')
#
#     def __str__(self):
#         return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True,)
    name_product = models.CharField(max_length=200)

    def __str__(self):
        return self.name_product
