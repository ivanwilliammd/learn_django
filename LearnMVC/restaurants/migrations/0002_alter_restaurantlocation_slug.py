# Generated by Django 3.2.13 on 2022-05-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]