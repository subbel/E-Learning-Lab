# Generated by Django 3.0.5 on 2024-01-24 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0015_auto_20220414_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
