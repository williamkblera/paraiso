# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-11 15:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0022_auto_20171211_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaproduto',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 12, 11, 15, 10, 6, 738453, tzinfo=utc)),
        ),
    ]
