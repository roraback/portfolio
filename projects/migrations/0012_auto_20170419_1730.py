# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20170419_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='testimonials',
            field=models.ManyToManyField(to='projects.Testimonial', null=True, blank=True),
            preserve_default=True,
        ),
    ]
