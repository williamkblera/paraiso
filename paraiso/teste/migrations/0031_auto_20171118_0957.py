# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-18 12:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0030_auto_20171117_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 18, 12, 57, 12, 582150, tzinfo=utc)),
        ),
    ]
