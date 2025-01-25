# Generated by Django 5.1.5 on 2025-01-25 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssfeed', '0003_folder_feed_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='folder',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='rssfeed.folder'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_folder', to='rssfeed.folder'),
        ),
    ]
