# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-26 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExioVisuals', '0028_auto_20160426_0501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=100)),
                ('url', models.TextField(editable=False)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='ExioVisuals.Country')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ('tree_id', 'lft'),
            },
        ),
        migrations.CreateModel(
            name='Selection2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.ManyToManyField(to='ExioVisuals.Country')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='country',
            unique_together=set([('name', 'slug', 'parent')]),
        ),
    ]
