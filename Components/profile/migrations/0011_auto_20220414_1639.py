# Generated by Django 3.0.5 on 2022-04-14 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0010_auto_20220404_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='/static/default_image.jpg', upload_to='profiles/'),
        ),
    ]
