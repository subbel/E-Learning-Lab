# Generated by Django 3.0.5 on 2021-03-08 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion_board', '0005_auto_20210307_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='reply',
            field=models.TextField(max_length=1000),
        ),
    ]
