# Generated by Django 4.0 on 2021-12-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeproducts',
            name='label',
            field=models.CharField(choices=[('sale', 'sale'), ('new', 'new'), ('None', 'None')], max_length=20),
        ),
    ]
