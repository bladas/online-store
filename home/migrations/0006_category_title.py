# Generated by Django 2.2.6 on 2019-10-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_category_name_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('status', 'status')], default='status', max_length=100),
        ),
    ]
