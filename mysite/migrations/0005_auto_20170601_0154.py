# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20170601_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_date2',
            field=models.CharField(default='time.localtime(time.time)', max_length=50),
        ),
    ]
