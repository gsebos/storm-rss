# Generated by Django 5.1.5 on 2025-01-26 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssfeed', '0009_feed_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
