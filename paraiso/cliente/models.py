# -*- coding:utf-8

from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    TIPO_PESSOA = (
        ('F', 'Pessoa Fisica'),
        ('J', 'Pessoa Juridica'),
    )
    nome = models.CharField(max_length=200)
    tipo_pessoa = models.CharField(max_length=1, choices=TIPO_PESSOA, default='F')
    data_criacao = models.DateTimeField(
        default=timezone.now()
    )

    def __str__(self):
        return self.nome

class Contato(models.Model):
    TIPO_CONTATO = (
        ('C', 'Celular'),
        ('E', 'Email'),
        ('W', 'Whatsapp'),
        ('F', 'Telefone Fixo'),
        ('O', 'Outro')
    )

    cliente = models.ForeignKey(Cliente)
    tipo_contato = models.CharField(max_length=1, choices=TIPO_CONTATO, default='C')
    contato = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.get_tipo_contato_display() + ": " + self.contato
