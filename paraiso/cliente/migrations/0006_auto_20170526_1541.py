# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 19:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20170526_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 26, 19, 41, 6, 371323, tzinfo=utc)),
        ),
    ]
