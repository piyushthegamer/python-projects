# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0008_registeration_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeration',
            name='image',
        ),
    ]
