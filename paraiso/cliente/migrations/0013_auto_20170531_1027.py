# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 14:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0012_auto_20170531_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 31, 14, 27, 13, 980361, tzinfo=utc)),
        ),
    ]
