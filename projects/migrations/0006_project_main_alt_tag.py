# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_main_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='main_alt_tag',
            field=models.CharField(default='I am an alt tag. Please replace me.', max_length=200),
            preserve_default=False,
        ),
    ]
