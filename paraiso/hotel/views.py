from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import datetime
from django.db.models import Q
import pytz

from .models import tipo_quarto, Quarto, Reserva, ReservaQuarto, ReservaPagamento


def calcula_dias(entrada, saida):
    diferenca = saida-entrada
    return diferenca.days

def calcula_turnos(entrada, saida):

    if entrada >= saida:
        turnos = 1
    else:
        diferenca=saida-entrada
        turnos = ((diferenca.total_seconds()/3600)/12)
    return turnos

def RemoveReservaLista(reservas, reserva):
    "Retorna uma nova lista de reservas sem a reserva passada"
    lista = []
    for item in reservas:
        if item!=reserva:
            lista.append(item)

    return lista

def CriarListaReservas(reservas):
    "Recebe uma queryset com a busca de ReservaQuarto e retorna uma lista para manipular"
    lista = []

    for reserva in reservas:
        r = {}
        r["cliente"] = reserva.reserva.cliente.nome
        r["quarto"] = reserva.quarto.nome
        # Descontando o UTC
        r["entrada"] = reserva.entrada.replace(second=0) - timezone.timedelta(hours=4)


        # Descontando o UTC
        r["saida"] = reserva.saida.replace(second=0)  - timezone.timedelta(hours=4)
        r["status"] = reserva.reserva.get_status_display()

        lista.append(r)



    return lista

def CriaTabela(entrada, saida):
    "Retrona uma tabela html com as reservas cadastradas entre as datas passadas"

    # Buscas as reservas que começam ou finalizam dentro da data buscada.
    reservas = ReservaQuarto.objects.filter(
        Q(entrada__range=[entrada-timezone.timedelta(days=1), saida+timezone.timedelta(days=1)])|
        Q(saida__range=[entrada, saida+timezone.timedelta(days=1)])|
        Q(entrada__lte=entrada,saida__gte=saida)
    )
    #.filter(
    #   saida__range=[dia-timezone.timedelta(days=2), fim+timezone.timedelta(days=2)]
    # ).order_by('entrada').order_by('quarto')
    print(len(reservas))
    # Cria uma lista com a reservas

    reservas = CriarListaReservas(reservas)



    # Busca todos os apartamento cadastrados
    apartamentos = Quarto.objects.all()

    # Armazenas as informações da tabela a ser exibida
    tabela=[]



    # laço que cria as linhas dos apartamentos da tabela
    for apartamento in apartamentos:
        data = entrada

        # Linha da tabela
        linha = []

        # Criando a primeira celula da linha com as informações do apartamento
        celula = {
            'quarto':apartamento.nome,
            'texto': apartamento.nome+"\n"+apartamento.get_status_display(),
            'status':apartamento.get_status_display(),
            'turnos':1, # Quantos turnos vão durar a reserva
        }

        linha.append(celula)



        # Laço que cria as celulas da linha
        while data <= saida+timezone.timedelta(hours=12):
            # Controle de if de comparação de datas
            achou = False
            # Laço para verificar se tem alguma reserva que cai nesta celula da tabela
            for reserva in reservas:



                if reserva["entrada"].strftime("%d-%m-%Y-%p") == data.strftime("%d-%m-%Y-%p"):

                    # Se a reserva for realmente para aquele apartamento
                    if str(reserva["quarto"]) == str(apartamento.nome):
                        # criando com a reserva.
                        celula = {
                            'data': data.strftime("%d-%m-%Y-%p"),
                            'quarto':reserva["quarto"],
                            'texto':"Cliente: " + reserva["cliente"]+
                                " Quarto: "+reserva["quarto"]+
                                " Entrada: "+reserva["entrada"].strftime("%d/%m/%Y")+
                                " Saida: "+reserva["saida"].strftime("%d/%m/%Y")+
                                " Status:"+reserva["status"],
                            'status': reserva["status"],
                            'turnos':calcula_turnos(reserva["entrada"],reserva["saida"]),
                        }
                        if reserva["saida"] > saida+timezone.timedelta(days=1):
                            celula["turnos"] = calcula_turnos(reserva["entrada"], saida+timezone.timedelta(days=1))

                        # Marca que achou uma reserva para esta celula
                        achou = True
                        reservas = RemoveReservaLista(reservas, reserva)
                        break



                if not(achou):

                    if reserva["entrada"] < entrada:
                        if reserva["quarto"] == apartamento.nome:
                            # criando com a reserva.
                            celula = {
                                'data': data.strftime("%d-%m-%Y-%p"),
                                'quarto':reserva["quarto"],
                                'texto':"Cliente: " + reserva["cliente"]+
                                    " Quarto: "+reserva["quarto"]+
                                    " Entrada: "+reserva["entrada"].strftime("%d/%m/%Y")+
                                    " Saida: "+reserva["saida"].strftime("%d/%m/%Y")+
                                    " Status:"+reserva["status"],
                                'status': reserva["status"],
                                # 'turnos':calcula_turnos(entrada,reserva["saida"]),
                            }
                            sai = reserva["saida"]
                            if reserva["saida"] > saida+timezone.timedelta(days=1):
                                sai = saida+timezone.timedelta(days=1)
                            ent = entrada

                            celula["turnos"] = calcula_turnos(ent, sai)
                            reservas = RemoveReservaLista(reservas, reserva)
                            achou = True

                            break


            # Se não achou uma celula antes, crie uma celula vazia
            if not(achou):
                # criando uma celula vazia.
                celula = {
                    'data': data.strftime("%d-%m-%Y-%p"),
                    'ap':apartamento.nome,
                    'texto':'',
                    'turnos':1,
                }




            linha.append(celula)

            # Soma a data uma quantidade de turno que foi usada pela celula
            data += timezone.timedelta(hours=celula["turnos"]*12)

        # adiciona a tabela a linha criada
        tabela.append(linha)

    # retorna a tabela pronta
    return tabela


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
            # print(timezone.now())
            # dia = datetime.strptime(timezone.now().strftime("%d/%m/%Y"), "%d/%m/%Y")
            dia = timezone.now()
            print(dia)

        # Adicionando informações de segundo na data
        dia = dia.replace(tzinfo=pytz.UTC)


        fim = dia + timezone.timedelta(days=6)

        # Adicionando informações de segundo na data
        fim = fim.replace(tzinfo=pytz.UTC)

        tabela = CriaTabela(dia, fim)

        days=[]

        # Hack para consertar a falta do UTC
        data = datetime.strptime(dia.strftime("%d/%m/%Y"), "%d/%m/%Y")


        for i in range(7):
            days.append(data) #.strftime("%a, %d/%m")
            data += timezone.timedelta(days=1)


        hoje = timezone.now()
        retroceder = (dia - timezone.timedelta(days=1)).strftime("%d/%m/%Y")
        avancar = (dia + timezone.timedelta(days=1)).strftime("%d/%m/%Y")

        context = {
            'hoje': hoje,
            'retroceder': retroceder,
            'avancar':avancar,
            'days':days,
            'dia':dia.strftime("%d/%m/%Y"),
            'fim':fim.strftime("%d/%m/%Y"),
            # 'quartos' : quartos,
            # 'reservas_quartos': reservas_quartos,
            'tabela': tabela,
        }
        return render(request, 'hotel/lista_hotel.html', context)
