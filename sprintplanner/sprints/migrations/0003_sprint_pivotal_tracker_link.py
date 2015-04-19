# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0002_auto_20150419_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='pivotal_tracker_link',
            field=models.URLField(default='https://www.pivotaltracker.com/dashboard'),
            preserve_default=False,
        ),
    ]
