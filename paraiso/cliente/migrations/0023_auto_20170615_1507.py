# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 19:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0022_auto_20170615_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 15, 19, 7, 5, 160181, tzinfo=utc)),
        ),
    ]