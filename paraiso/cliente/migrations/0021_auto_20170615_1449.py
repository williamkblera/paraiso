# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 18:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0020_auto_20170615_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 15, 18, 49, 6, 852327, tzinfo=utc)),
        ),
    ]