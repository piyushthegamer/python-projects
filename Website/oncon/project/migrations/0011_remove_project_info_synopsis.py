# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 22:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20160430_0339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_info',
            name='synopsis',
        ),
    ]
