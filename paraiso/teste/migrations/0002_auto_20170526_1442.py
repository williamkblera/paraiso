# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 18:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 26, 18, 42, 8, 513776, tzinfo=utc)),
        ),
    ]