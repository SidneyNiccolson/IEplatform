# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExioVisuals', '0026_auto_20160415_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=100),
        ),
    ]
