# Generated by Django 3.0.5 on 2021-04-09 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_courses_users'),
        ('student', '0019_quiz_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='courses',
            field=models.ForeignKey(default='dd390af4-07f1-4597-b48a-f585fd79289d', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='courses.Courses'),
        ),
    ]
