# Generated by Django 3.0.5 on 2023-05-05 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppifyPage', '0009_auto_20230421_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingpage',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
    ]
