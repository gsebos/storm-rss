# Generated by Django 5.1.5 on 2025-01-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssfeed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
