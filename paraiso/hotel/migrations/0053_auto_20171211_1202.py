# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-11 15:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0052_auto_20171211_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 11, 15, 2, 39, 414839, tzinfo=utc), verbose_name='Data da Reserva'),
        ),
    ]
