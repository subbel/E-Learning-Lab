# Generated by Django 3.0.5 on 2022-03-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20210408_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='Hey, this is my bio...', max_length=250),
        ),
    ]
