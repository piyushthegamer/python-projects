# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20160430_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_info',
            name='synopsis',
            field=models.FileField(max_length=500, upload_to='synfiles'),
        ),
    ]