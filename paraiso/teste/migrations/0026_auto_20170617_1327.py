# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 17:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0025_auto_20170617_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 17, 17, 27, 56, 930121, tzinfo=utc)),
        ),
    ]
