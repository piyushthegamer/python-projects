# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registeration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('uid', models.CharField(max_length=30)),
                ('eid', models.CharField(max_length=50)),
                ('cnum', models.CharField(max_length=12)),
                ('pwd', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=6)),
                ('dob', models.CharField(max_length=10)),
                ('pid', models.CharField(max_length=10)),
            ],
        ),
    ]
