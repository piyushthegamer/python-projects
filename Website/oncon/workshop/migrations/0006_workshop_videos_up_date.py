# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0005_auto_20160426_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop_videos',
            name='up_date',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
