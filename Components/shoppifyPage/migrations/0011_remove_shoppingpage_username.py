# Generated by Django 3.0.5 on 2023-05-05 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppifyPage', '0010_shoppingpage_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingpage',
            name='username',
        ),
    ]
