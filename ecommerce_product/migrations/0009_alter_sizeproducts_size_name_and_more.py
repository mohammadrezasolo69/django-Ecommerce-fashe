# Generated by Django 4.0 on 2021-12-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_product', '0008_alter_storeproducts_size_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizeproducts',
            name='size_name',
            field=models.CharField(choices=[('M ', 'M'), ('L', 'L'), ('XL', 'XL'), ('XL', '2XL'), ('3XL', '3XL')], max_length=10),
        ),
        migrations.AlterField(
            model_name='storeproducts',
            name='size_color',
            field=models.ManyToManyField(to='ecommerce_product.SizeProducts'),
        ),
    ]
