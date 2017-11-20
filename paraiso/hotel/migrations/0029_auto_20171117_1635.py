# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-17 19:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0028_auto_20170621_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 17, 19, 35, 12, 705761, tzinfo=utc), verbose_name='Data da Reserva'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='status',
            field=models.CharField(choices=[('R', 'Pré-reserva'), ('P', 'Confirmada'), ('N', 'No-Show'), ('W', 'Walk-in'), ('F', 'Finalizada'), ('C', 'Cancelada'), ('D', 'Deadline vencida')], max_length=1),
        ),
    ]