# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-18 16:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0034_auto_20171118_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('tipo_produto', models.CharField(choices=[('F', 'Produto Fisico'), ('S', 'Serviço')], default='F', max_length=1, verbose_name='É um ')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Preço')),
                ('limite_dia', models.IntegerField(default=-1, verbose_name='Limite por dia')),
                ('status', models.CharField(choices=[('A', 'Ativo'), ('D', 'Desativado')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ReservaProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, default=datetime.datetime(2017, 11, 18, 16, 42, 42, 403842, tzinfo=utc))),
                ('qtd', models.PositiveIntegerField()),
                ('custo', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserva_produto', to='cliente.Cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserva', to='produto.Produto')),
            ],
        ),
    ]
