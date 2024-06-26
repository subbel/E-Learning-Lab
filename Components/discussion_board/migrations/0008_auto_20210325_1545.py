# Generated by Django 3.0.5 on 2021-03-25 22:45

from django.db import migrations, models
import profanity.validators


class Migration(migrations.Migration):

    dependencies = [
        ('discussion_board', '0007_auto_20210309_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=1000, validators=[profanity.validators.validate_is_profane]),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='content',
            field=models.CharField(max_length=1000, validators=[profanity.validators.validate_is_profane]),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply',
            field=models.TextField(max_length=1000, validators=[profanity.validators.validate_is_profane]),
        ),
    ]
