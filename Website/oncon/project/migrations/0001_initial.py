# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=12)),
                ('ptitle', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=12)),
                ('rating', models.CharField(max_length=5)),
                ('members', models.CharField(max_length=3)),
                ('synopsis', models.FileField(upload_to='synfiles')),
                ('detail', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=80)),
                ('video', models.FileField(upload_to='videos')),
                ('status', models.CharField(max_length=10)),
                ('technology', models.CharField(max_length=40)),
                ('image', models.FileField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='projectlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proid', models.CharField(max_length=6)),
                ('pid', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='projectsubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proid', models.CharField(max_length=6)),
                ('ptitle', models.CharField(max_length=40)),
                ('members', models.CharField(max_length=4)),
                ('ratings', models.CharField(max_length=4)),
                ('date', models.CharField(max_length=12)),
                ('images', models.FileField(default='images/images.jpg', upload_to='images')),
                ('status', models.CharField(max_length=10)),
                ('pid', models.CharField(max_length=40)),
            ],
        ),
    ]
