from datetime import datetime
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class UnderCategory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True )
    def __str__(self):
        return self.title


class Product(models.Model):
    ucategory = models.ForeignKey(UnderCategory, on_delete=models.CASCADE, blank=True, null=True )
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name
