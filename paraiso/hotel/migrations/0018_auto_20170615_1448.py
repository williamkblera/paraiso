# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 18:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0017_auto_20170614_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 15, 18, 48, 56, 854969, tzinfo=utc), verbose_name='Data da Reserva'),
        ),
    ]
