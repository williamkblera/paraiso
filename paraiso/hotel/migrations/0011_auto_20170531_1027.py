# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 14:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_auto_20170531_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 31, 14, 27, 13, 991210, tzinfo=utc), verbose_name='Data da Reserva'),
        ),
    ]