# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 14:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0013_auto_20170601_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 4, 14, 26, 53, 987958, tzinfo=utc)),
        ),
    ]
