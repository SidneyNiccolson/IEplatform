# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-17 11:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExioVisuals', '0031_auto_20160517_0627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('tree_id', 'lft'), 'verbose_name_plural': 'FancyTreeCountry'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('tree_id', 'lft'), 'verbose_name_plural': 'FancyTreeProduct'},
        ),
    ]