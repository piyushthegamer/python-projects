# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20160426_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imagestore',
            field=models.FileField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
