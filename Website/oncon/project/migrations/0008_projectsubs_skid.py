# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_remove_projectsubs_profid'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsubs',
            name='skid',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]