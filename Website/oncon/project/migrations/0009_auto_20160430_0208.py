# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_projectsubs_skid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectsubs',
            old_name='ratings',
            new_name='rating',
        ),
    ]
