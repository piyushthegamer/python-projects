# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_workshop_detail_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop_detail',
            name='images',
            field=models.FileField(default='images/images.jpg', upload_to='images'),
        ),
    ]
