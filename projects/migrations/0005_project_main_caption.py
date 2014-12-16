# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20141126_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='main_caption',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
