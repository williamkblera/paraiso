# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-10 19:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0017_auto_20171210_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaproduto',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 12, 10, 19, 21, 54, 315609, tzinfo=utc)),
        ),
    ]