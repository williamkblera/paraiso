# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 13:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0013_auto_20170531_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 1, 13, 10, 13, 168480, tzinfo=utc)),
        ),
    ]
