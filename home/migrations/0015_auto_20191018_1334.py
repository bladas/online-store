# Generated by Django 2.2.6 on 2019-10-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20191017_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('Ноутбуки и компьютеры', 'Ноутбуки и компьютеры'), ('Бытовая техника', 'Бытовая техника'), ('Смартфоны, ТВ и электроника', 'Смартфоны, ТВ и электроника'), ('Товары для дома', 'Товары для дома'), ('Инструменты и автотовары', 'Инструменты и автотовары'), ('Сантехника и ремонт', 'Сантехника и ремонт'), ('Дача, сад и огорд', 'Дача, сад и огорд'), ('Спорт и увлечения', 'Спорт и увлечения'), ('Одежда, обувь и уркашения', 'Одежда, обувь и уркашения'), ('Красота и здоровье', 'Красота и здоровье'), ('Детские товары', 'Детские товары'), ('Канцтовары и книги', 'Канцтовары и книги'), ('Алкогольные напитки и продукты', 'Алкогольные напитки и продукты'), ('Товары для бизнеса', 'Товары для бизнеса')], default='Ноутбуки и компьютеры', max_length=100),
        ),
    ]
