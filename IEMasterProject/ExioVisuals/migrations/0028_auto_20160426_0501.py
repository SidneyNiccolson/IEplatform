# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-26 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExioVisuals', '0027_auto_20160415_1255'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='selection',
            old_name='categories',
            new_name='products',
        ),
    ]