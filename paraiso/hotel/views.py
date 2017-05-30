from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import datetime

from .models import *

def reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    quartos = ReservaQuarto.objects.filter(reserva__pk=pk)
    context = {
        'reserva':reserva,
        'quartos':quartos,
    }
    return render(request, 'hotel/reserva.html', context)

def lista_reservas(request, data=None):

        if request.method == "POST":
            data = request.POST.get('data')
            dia = datetime.strptime(data, "%d/%m/%Y")
        if data == None:
            dia = timezone.now()
        
        # quartos = Quartos.objects.filter(reservaquarto__)
        quartos = ReservaQuarto.objects.filter(entrada__date=dia)
        # quartos = ReservaQuarto.objects.all()
        # quartos = ReservaQuarto.objects.filter().exclude(
        #     reserva__status='F'
        # ).exclude(
        #     reserva__status='C'
        # )
        context = {
            # 'reservas': reservas,
            'dia':dia.strftime("%d/%m/%Y"),
            'quartos' : quartos,
        }
        return render(request, 'hotel/lista_hotel.html', context)
