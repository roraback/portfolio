# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20170410_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tagline',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
