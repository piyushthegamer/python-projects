# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='image',
            field=models.FileField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
