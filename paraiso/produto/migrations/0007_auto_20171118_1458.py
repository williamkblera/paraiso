# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-18 17:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_auto_20171118_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaproduto',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 11, 18, 17, 58, 45, 42799, tzinfo=utc)),
        ),
    ]
