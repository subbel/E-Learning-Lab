# Generated by Django 3.0.5 on 2023-05-05 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppifyPage', '0014_auto_20230505_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingpage',
            name='username',
        ),
    ]
