# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0006_workshop_videos_up_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop_videos',
            name='vid_title',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
