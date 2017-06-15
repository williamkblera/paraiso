# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 00:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0016_auto_20170604_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 15, 0, 39, 5, 950864, tzinfo=utc), verbose_name='Data da Reserva'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='status',
            field=models.CharField(choices=[('R', 'Pré-reserva'), ('P', 'Confirmada'), ('N', 'No-Show'), ('W', 'Walk-in'), ('O', 'Ocupado'), ('F', 'Finalizada'), ('C', 'Cancelada'), ('D', 'Deadline vencida')], max_length=1),
        ),
    ]