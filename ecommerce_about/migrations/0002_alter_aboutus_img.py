# Generated by Django 4.0 on 2022-01-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='img',
            field=models.ImageField(upload_to='about_us/'),
        ),
    ]
