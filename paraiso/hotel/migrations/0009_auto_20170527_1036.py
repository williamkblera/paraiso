# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 14:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_auto_20170527_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 27, 14, 36, 1, 383718, tzinfo=utc), verbose_name='Data da Reserva'),
        ),
        migrations.AlterField(
            model_name='reservapagamento',
            name='reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamentos', to='hotel.Reserva'),
        ),
        migrations.AlterField(
            model_name='reservapagamento',
            name='reserva_quarto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamento', to='hotel.ReservaQuarto'),
        ),
    ]
