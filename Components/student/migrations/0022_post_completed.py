# Generated by Django 3.0.5 on 2022-04-04 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_merge_20210408_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
