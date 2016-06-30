# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-09 11:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ExioVisuals', '0033_auto_20160609_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='local',
        ),
        migrations.AddField(
            model_name='country',
            name='local',
            field=models.CharField(default=datetime.datetime(2016, 6, 9, 11, 42, 19, 765596, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='level',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='level',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
    ]
