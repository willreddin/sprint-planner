# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('displayName', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('summary', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('start', models.DateTimeField(verbose_name='start date')),
                ('end', models.DateTimeField(verbose_name='end date')),
                ('organizer', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='attendee',
            name='sprint',
            field=models.ForeignKey(to='sprints.Sprint'),
        ),
    ]
