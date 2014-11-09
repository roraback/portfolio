# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addendum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('attachment', models.FileField(null=True, upload_to=b'addenda', blank=True)),
                ('rank', models.IntegerField()),
            ],
            options={
                'ordering': ['rank'],
                'verbose_name_plural': 'addenda',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('rank', models.IntegerField()),
            ],
            options={
                'ordering': ['rank'],
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(default=b'img/default.jpg', upload_to=b'images')),
                ('thumbnail', models.ImageField(default=b'img/defaultThumb.jpg', null=True, upload_to=b'images', blank=True)),
                ('caption', models.TextField()),
                ('rank', models.IntegerField()),
            ],
            options={
                'ordering': ['rank'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('challenges', models.TextField(null=True, blank=True)),
                ('solutions', models.TextField(null=True, blank=True)),
                ('has_video', models.BooleanField(default=True)),
                ('video_embed_code', models.TextField(null=True, blank=True)),
                ('thumbnail', models.ImageField(default=b'img/defaultThumb.jpg', null=True, upload_to=b'projects', blank=True)),
                ('main_image', models.ImageField(default=b'img/default.jpg', null=True, upload_to=b'projects', blank=True)),
                ('rank', models.IntegerField()),
                ('category', models.ForeignKey(to='projects.Category')),
            ],
            options={
                'ordering': ['rank'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='addendum',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
            preserve_default=True,
        ),
    ]
