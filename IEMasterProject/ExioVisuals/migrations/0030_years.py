# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-10 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExioVisuals', '0029_auto_20160426_0552'),
    ]

    operations = [
        migrations.CreateModel(
            name='years',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.CharField(max_length=128, unique=True)),
            ],
        ),
    ]
