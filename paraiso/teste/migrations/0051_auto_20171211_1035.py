# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-11 13:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0050_auto_20171210_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 11, 13, 35, 6, 977444, tzinfo=utc)),
        ),
    ]
