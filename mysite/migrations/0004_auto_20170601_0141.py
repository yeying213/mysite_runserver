# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import time


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20170531_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name_plural': 'F1_反馈'},
        ),
        migrations.AddField(
            model_name='news',
            name='published_date2',
            field=models.IntegerField(default=time.time),
        ),
    ]
