# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 12:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PUMA', '0003_remove_weatherstation_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='picture',
            field=models.ImageField(default=datetime.datetime(2016, 3, 12, 12, 38, 49, 760166, tzinfo=utc), upload_to=''),
            preserve_default=False,
        ),
    ]
