# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_main_alt_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='login_required',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
