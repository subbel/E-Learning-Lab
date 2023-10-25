# Generated by Django 3.0.5 on 2023-04-19 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppifyPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingpage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='shoppingpage',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='shoppingpage',
            name='title',
        ),
        migrations.AddField(
            model_name='shoppingpage',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='shoppingpage',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=4),
        ),
    ]
