# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20160426_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videostore',
            field=models.FileField(default=1, upload_to='videos'),
            preserve_default=False,
        ),
    ]