# Generated by Django 3.0.5 on 2023-04-19 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppifyPage', '0003_remove_shoppingpage_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingpage',
            name='price',
            field=models.CharField(default='', max_length=255),
        ),
    ]
