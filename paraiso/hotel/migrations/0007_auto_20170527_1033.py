# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 14:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20170527_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quartos', to='hotel.tipo_quarto'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='cliente.Cliente'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 27, 14, 33, 2, 312218, tzinfo=utc), verbose_name='Data da Reserva'),
        ),
    ]