# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-10 14:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0047_auto_20171119_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 10, 14, 56, 3, 218132, tzinfo=utc)),
        ),
    ]
