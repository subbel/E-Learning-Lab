# Generated by Django 3.0.5 on 2020-06-28 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
