# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-18 17:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0036_auto_20171118_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 18, 17, 43, 52, 853722, tzinfo=utc)),
        ),
    ]
