# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_project_info_videodate'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_info',
            name='note',
            field=models.CharField(default='Blah', max_length=100),
            preserve_default=False,
        ),
    ]
