# Generated by Django 3.0.5 on 2023-05-05 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppifyPage', '0011_remove_shoppingpage_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingpage',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
    ]