# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-18 16:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaproduto',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 11, 18, 16, 46, 11, 331843, tzinfo=utc)),
        ),
    ]
