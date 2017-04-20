# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('by_name', models.CharField(max_length=100)),
                ('by_position', models.CharField(max_length=100)),
                ('by_company', models.CharField(max_length=100)),
                ('rank', models.IntegerField()),
            ],
            options={
                'ordering': ['rank'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='testimonials',
            field=models.ManyToManyField(to='projects.Testimonial'),
            preserve_default=True,
        ),
    ]
