# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 16:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0016_auto_20170604_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 4, 16, 2, 6, 477400, tzinfo=utc)),
        ),
    ]