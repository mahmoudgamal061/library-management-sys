# Generated by Django 4.2 on 2023-06-16 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0006_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
