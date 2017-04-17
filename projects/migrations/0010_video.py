# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_tagline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('embed_id', models.CharField(max_length=100)),
                ('caption', models.TextField()),
                ('rank', models.IntegerField()),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
                'ordering': ['rank'],
            },
            bases=(models.Model,),
        ),
    ]
