# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ExioVisuals', '0007_remove_weatherstation_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('geom', djgeojson.fields.PolygonField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='popup',
        ),
    ]