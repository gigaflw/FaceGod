# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-02 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_photostatistic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='score',
            field=models.CharField(max_length=20),
        ),
    ]
