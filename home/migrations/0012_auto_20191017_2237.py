# Generated by Django 2.2.6 on 2019-10-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20191017_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('Ноутбуки и компьютеры', 'Ноутбуки и компьютеры'), ('Бытовая техника', 'Бытовая техника')], default='Ноутбуки и компьютеры', max_length=100),
        ),
    ]
