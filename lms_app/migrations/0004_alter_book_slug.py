# Generated by Django 4.2 on 2023-06-15 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0003_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, default='No-SLUG', null=True),
        ),
    ]
