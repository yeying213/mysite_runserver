# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_content', models.CharField(max_length=300)),
                ('feed_contact', models.CharField(max_length=100)),
                ('feed_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'F_反馈',
            },
        ),
    ]