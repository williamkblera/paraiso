# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-18 17:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0034_auto_20171118_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 18, 17, 43, 25, 958719, tzinfo=utc)),
        ),
    ]
