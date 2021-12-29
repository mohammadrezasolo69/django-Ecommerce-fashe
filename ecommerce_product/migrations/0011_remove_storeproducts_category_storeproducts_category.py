# Generated by Django 4.0 on 2021-12-28 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_product', '0010_remove_storeproducts_category_storeproducts_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeproducts',
            name='category',
        ),
        migrations.AddField(
            model_name='storeproducts',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scategory', to='ecommerce_product.categoryproducts'),
        ),
    ]
