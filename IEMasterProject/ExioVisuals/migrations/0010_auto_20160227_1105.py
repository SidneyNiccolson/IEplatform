# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 17:05
from __future__ import unicode_literals

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ExioVisuals', '0009_auto_20160227_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='geom',
            field=djgeojson.fields.PolygonField(),
        ),
    ]
