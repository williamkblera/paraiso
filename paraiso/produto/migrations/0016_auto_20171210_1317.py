# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-10 16:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0015_auto_20171210_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaproduto',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 12, 10, 16, 17, 20, 295645, tzinfo=utc)),
        ),
    ]
