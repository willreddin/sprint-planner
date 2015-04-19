# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendee',
            old_name='sprint',
            new_name='assigned_sprint',
        ),
    ]
