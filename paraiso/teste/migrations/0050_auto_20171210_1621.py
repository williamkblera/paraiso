# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-10 19:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0049_auto_20171210_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 10, 19, 21, 54, 283985, tzinfo=utc)),
        ),
    ]
