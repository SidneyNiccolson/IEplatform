# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExioVisuals', '0015_area_color'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='WeatherStation',
        ),
    ]
