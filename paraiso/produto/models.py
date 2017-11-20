from django.db import models
from django.utils import timezone

from cliente.models import Cliente

class Produto(models.Model):

    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    TIPO_PRODUTO = (
        ('F', 'Produto Fisico'),
        ('S', 'Serviço'),
    )
    tipo_produto = models.CharField(
        max_length=1,
        choices=TIPO_PRODUTO,
        default='F',
        verbose_name="É um ",
    )
    preco = models.DecimalField(
        verbose_name="Preço",
        decimal_places=2,
        max_digits=20,
    )
    limite_dia = models.IntegerField(
    # Quantos produtos/serviços deste podem ser vendidos por dia?
        verbose_name="Limite por dia",
        default=0, # 0 não tem limites; 0 > limite/dia
    )
    STATUS_PRODUTO = (
        ('A', 'Ativo'),
        ('D', 'Desativado'),
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_PRODUTO,
        default='A',
    )

    def __str__(self):
        return self.nome


class ReservaProduto(models.Model):
    produto = models.ForeignKey(Produto, related_name="reserva")
    cliente = models.ForeignKey(Cliente, related_name="reserva_produto")
    data = models.DateField(
        default=timezone.now(),
    )
    qtd = models.PositiveIntegerField()
    desconto = models.DecimalField(
        decimal_places=2,
        max_digits=20,
        default=0.0,
    )
    total = models.DecimalField(
        decimal_places=2,
        max_digits=20,
    )
    STATUS_RESERVA = (
        ('P', 'Pré-reserva'), # Falta pagar o sinal
        ('C', 'Confirmada'),  # Feito o pagamento de sinal
        ('O', 'Paga'), # Totalmente Pago e Finalizada
        ('E', 'Cancelada'), # a reserva foi Cancelada
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_RESERVA,
        default='P',
    )


    def __str__(self):
        return str(self.data) + \
        ": " + str(self.cliente) + \
        " - " + str(self.produto) + \
        ": " + str(self.qtd)
