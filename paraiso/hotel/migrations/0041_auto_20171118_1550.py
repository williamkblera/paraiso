# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-18 18:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0040_auto_20171118_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 18, 18, 50, 17, 50860, tzinfo=utc), verbose_name='Data da Reserva'),
        ),
    ]
