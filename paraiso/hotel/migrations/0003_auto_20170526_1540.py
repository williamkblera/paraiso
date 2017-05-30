# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 19:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20170526_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 26, 19, 40, 14, 999233, tzinfo=utc), verbose_name='Data da Reserva'),
        ),
        migrations.AlterField(
            model_name='reservaquarto',
            name='qtd_adultos',
            field=models.PositiveIntegerField(default=1, verbose_name='Qtd. Adultos'),
        ),
        migrations.AlterField(
            model_name='reservaquarto',
            name='qtd_crianca',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Qtd. Crianças'),
        ),
        migrations.AlterField(
            model_name='reservaquarto',
            name='saida',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
