# Generated by Django 3.2.13 on 2022-05-15 08:48

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('my_date_field', models.DateField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
        ),
    ]
