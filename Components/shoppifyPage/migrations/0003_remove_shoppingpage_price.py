# Generated by Django 3.0.5 on 2023-04-19 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppifyPage', '0002_auto_20230418_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingpage',
            name='price',
        ),
    ]
