from django.db import models
from django.utils import timezone

from cliente.models import Cliente



class tipo_quarto(models.Model):
    tipo = models.CharField(max_length=100, unique=True)
    descrição = models.TextField(blank=True, null=True)
    preco_base = models.DecimalField(
        verbose_name="Preço Base",
        decimal_places=2,
        max_digits=20
    )
    pessoa_adicional = models.DecimalField(
        verbose_name="Custo Pessoa Adicional",
        decimal_places=2,
        max_digits=20
    )

    def __str__(self):
        return self.tipo


class Quarto(models.Model):
    STATUS_QUARTO = (
        ('A', 'Ativo'),
        ('S', 'Sujo'),
        ('M', 'Esperando Manutenção'),
        ('O', 'Ocupado'),
    )
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.ForeignKey(tipo_quarto, related_name="quartos")
    descricao = models.TextField()
    cama_casal = models.IntegerField(
        verbose_name="Qtd. camas de casal",
        default=1)
    cama_solteiro = models.IntegerField(
        verbose_name="Qtd. camas de solteiro",
        default=0)
    status = models.CharField(max_length=1, choices=STATUS_QUARTO)

    def __str__(self):
        return self.nome


    def PaxTotal(self, **kwargs):
        "Retorna PAX total do quarto"
        return ((self.cama_casal*2)+self.cama_solteiro)


def calcula_deadline():
    # Soma um dia ao dead line padrão
    return timezone.now()+timezone.timedelta(days=1)



class Reserva(models.Model):
    STATUS_RESERVA = (
        ('R', 'Pré-reserva'),
        ('P', 'Confirmada'),
        ('N', 'No-Show'),
        ('W', 'Walk-in'),
        ('F', 'Finalizada'),
        ('C', 'Cancelada'),
        ('D', 'Deadline vencida'),
    )
    cliente = models.ForeignKey(Cliente, related_name="reservas")
    data_reserva = models.DateTimeField(
        verbose_name="Data da Reserva",
        default=timezone.now()
    )
    status = models.CharField(max_length=1, choices=STATUS_RESERVA)
    dead_line = models.DateField(
        verbose_name="Dead Line",
        default=calcula_deadline
        )
    historico = models.TextField(
        blank=True, null=True
    )

    def __str__(self):
        return self.cliente.nome + " - " + self.data_reserva.strftime('%d/%m/%y')


class ReservaQuarto(models.Model):
    reserva = models.ForeignKey(Reserva, related_name="quartos")
    quarto = models.ForeignKey(Quarto, related_name="reservas")
    entrada = models.DateTimeField(
        default=timezone.now
    )
    saida = models.DateTimeField(
        default=timezone.now
    )
    qtd_adultos = models.PositiveIntegerField(
        verbose_name="Qtd. Adultos",
        default=1,
    )
    qtd_crianca = models.PositiveIntegerField(
        verbose_name="Qtd. Crianças",
        default=0,
        blank=True
    )
    checkin = models.DateTimeField(
        blank=True,
        null=True
    )
    checkout = models.DateTimeField(
        blank=True,
        null=True
    )
    custo = models.DecimalField(
        decimal_places=2,
        max_digits=20
    )

    def __str__(self):
        return self.quarto.nome + " - " + self.entrada.strftime('%d/%m/%y')

    def set_checkin(self):
        "Faz check in no quarto"

        # Se apartamento está ativo e livre
        if self.quarto.status == 'A':
            # Marca apartamento como Ocupado
            self.quarto.status = 'O'
            self.quarto.save()

            # Salva horario de check in
            self.checkin = timezone.now()
            self.save()
            return True
        else:
            return False

    def set_checkout(self):
        "Faz check out no quarto"

        # Se apartamento está Ocupado
        if self.quarto.status == 'O':
            # Marca apartamento como Sujo
            self.quarto.status = 'S'
            self.quarto.save()
            # Salva horario de check out
            self.checkout = timezone.now()
            self.save()
            return True
        else:
            return False

class ReservaPagamento(models.Model):
    STATUS_PAGAMENTO = (
        ('A', 'Agendado para'),
        ('P', 'Pago'),
    )
    reserva = models.ForeignKey(Reserva, related_name="pagamentos")
    reserva_quarto = models.ForeignKey(ReservaQuarto, related_name="pagamento")
    pagamento = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )
    data_pagamento = models.DateField(
        default=timezone.now
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_PAGAMENTO,
        default='A'
    )
    descricao = models.TextField(
        blank=True,
        null=True
    )
