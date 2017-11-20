# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-18 12:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0029_auto_20171117_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarto',
            name='status',
            field=models.CharField(choices=[('A', 'Ativo'), ('S', 'Sujo'), ('M', 'Esperando Manutenção')], max_length=1),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 18, 12, 57, 12, 584667, tzinfo=utc), verbose_name='Data da Reserva'),
        ),
    ]
