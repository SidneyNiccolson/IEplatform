# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-09 11:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ExioVisuals', '0034_auto_20160609_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='lvl',
            field=models.CharField(default=datetime.datetime(2016, 6, 9, 11, 43, 54, 632690, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='level',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
    ]
