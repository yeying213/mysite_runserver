# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 11:22
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IS_TOP', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='N', max_length=5)),
                ('title', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('main_img', models.ImageField(blank=True, upload_to='blog_main_img')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容')),
                ('blog_read', models.IntegerField(default=0)),
                ('blog_up', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'D2_博客内容(编辑)',
                'ordering': ['-IS_TOP', '-published_date'],
            },
        ),
        migrations.CreateModel(
            name='Blog_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('comment_text', models.TextField(blank=True)),
                ('blog_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Blog')),
            ],
            options={
                'verbose_name_plural': 'D3_博客评论',
                'ordering': ['-comment_time'],
            },
        ),
        migrations.CreateModel(
            name='Blog_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('tag_img', models.FileField(blank=True, upload_to='tag_img')),
                ('rank', models.IntegerField(default=99)),
            ],
            options={
                'verbose_name_plural': 'D1_博客标签',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('IS_TOP', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='N', max_length=5)),
                ('main_img', models.ImageField(blank=True, upload_to='news_main_img')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容')),
            ],
            options={
                'verbose_name_plural': 'C3_新闻内容(编辑)',
                'ordering': ['-published_date'],
            },
        ),
        migrations.CreateModel(
            name='News_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('comment_text', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'C4_新闻评论',
                'ordering': ['-comment_time'],
            },
        ),
        migrations.CreateModel(
            name='News_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('tag_img', models.FileField(blank=True, upload_to='tag_img')),
                ('rank', models.IntegerField(default=99)),
            ],
            options={
                'verbose_name_plural': 'C1_新闻标签',
            },
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'C2_新闻来源',
            },
        ),
        migrations.CreateModel(
            name='Reg_vip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('reg_time', models.DateTimeField(auto_now_add=True)),
                ('user_img', models.FileField(blank=True, upload_to='author_img')),
            ],
            options={
                'verbose_name_plural': 'A_注册会员',
                'ordering': ['-reg_time'],
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_title', models.CharField(blank=True, max_length=20)),
                ('share_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('share_desc', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Reg_vip')),
            ],
            options={
                'verbose_name_plural': 'E3_分享',
            },
        ),
        migrations.CreateModel(
            name='Share_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_file', models.FileField(blank=True, upload_to='share_file')),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Share')),
            ],
            options={
                'verbose_name_plural': 'E2_分享文件',
            },
        ),
        migrations.CreateModel(
            name='Share_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'E1_分享标签',
            },
        ),
        migrations.CreateModel(
            name='Sort_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('rank', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'B2_分类名称',
                'ordering': ['rank'],
            },
        ),
        migrations.CreateModel(
            name='Sort_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('url', models.URLField()),
                ('logo', models.FileField(blank=True, upload_to='url_logo')),
                ('rank', models.IntegerField()),
                ('sort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Sort_tag')),
            ],
            options={
                'verbose_name_plural': 'B3_分类网址',
                'ordering': ['sort', 'rank'],
            },
        ),
        migrations.CreateModel(
            name='Top_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('url', models.URLField()),
                ('logo', models.FileField(blank=True, upload_to='url_logo')),
                ('rank', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'B1_热门网址',
                'ordering': ['rank'],
            },
        ),
        migrations.AddField(
            model_name='share',
            name='share_tag',
            field=models.ManyToManyField(to='mysite.Share_tag'),
        ),
        migrations.AddField(
            model_name='news_comment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Reg_vip'),
        ),
        migrations.AddField(
            model_name='news_comment',
            name='news_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.News'),
        ),
        migrations.AddField(
            model_name='news',
            name='news_tag',
            field=models.ManyToManyField(to='mysite.News_tag'),
        ),
        migrations.AddField(
            model_name='news',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Origin'),
        ),
        migrations.AddField(
            model_name='blog_comment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Reg_vip'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Reg_vip'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_tag',
            field=models.ManyToManyField(blank=True, to='mysite.Blog_tag', verbose_name='博客标签'),
        ),
    ]
