# Generated by Django 5.0.1 on 2024-01-11 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='description',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question_description',
        ),
        migrations.RemoveField(
            model_name='tests',
            name='description_test',
        ),
    ]
