# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-18 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PUMA', '0013_auto_20160518_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='affiliation',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='comment',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='...@...', max_length=254),
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.CharField(default='', max_length=200),
        ),
    ]