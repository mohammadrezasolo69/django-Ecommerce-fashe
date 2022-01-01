# Generated by Django 4.0 on 2022-01-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('img', models.ImageField(upload_to='about_us')),
                ('descriptions_main', models.TextField()),
                ('descriptions_long', models.TextField()),
            ],
        ),
    ]