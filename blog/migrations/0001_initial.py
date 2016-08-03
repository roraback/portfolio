# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, db_index=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created', models.DateField(auto_now_add=True)),
                ('posted', models.DateField(default=datetime.date.today, db_index=True)),
                ('slug', models.SlugField(max_length=255, unique=True, null=True, blank=True)),
                ('login_required', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['posted'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('rank', models.IntegerField(blank=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100)),
                ('rank', models.IntegerField(blank=True)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='blog.BlogCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.BlogTag'),
            preserve_default=True,
        ),
    ]
