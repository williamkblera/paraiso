# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 19:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0027_auto_20170617_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 17, 19, 30, 29, 792777, tzinfo=utc)),
        ),
    ]
