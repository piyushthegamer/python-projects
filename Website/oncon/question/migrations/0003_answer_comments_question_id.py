# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20160421_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer_comments',
            name='question_id',
            field=models.CharField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]
