# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='skill_karma_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=12)),
                ('skill', models.CharField(max_length=5)),
                ('karma', models.CharField(max_length=5)),
                ('total', models.CharField(max_length=5)),
            ],
        ),
    ]
