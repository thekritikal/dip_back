# Generated by Django 3.2.2 on 2021-05-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='all', max_length=244),
        ),
    ]
