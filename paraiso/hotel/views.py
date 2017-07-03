from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.utils.formats import localize
from datetime import datetime
from django.db.models import Q
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from urllib.parse import quote
import json
import pytz


from .models import tipo_quarto, Quarto, Reserva, ReservaQuarto, ReservaPagamento
from .forms import QuartoForm, ReservaForm

def calcula_turnos(entrada, saida):
    "Retorna a quantidade de turnos de 12 horas que a reserva vai durar"
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
        r['pk'] = reserva.pk
        r["cliente"] = reserva.reserva.cliente.nome
        r["quarto"] = reserva.quarto.nome
        # Descontando o UTC
        r["entrada"] = reserva.entrada.replace(second=0) - timezone.timedelta(hours=4)


        # Descontando o UTC
        r["saida"] = reserva.saida.replace(second=0)  - timezone.timedelta(hours=4)
        r['checkin'] = reserva.checkin
        r['checkout'] = reserva.checkout
        r["status"] = reserva.reserva.get_status_display()
        r["status_ap"] = reserva.quarto.get_status_display()

        lista.append(r)

    return lista

def CriaTabela(entrada, saida):
    "Retorna uma tabela html com as reservas cadastradas entre as datas passadas"

    # Buscas as reservas que começam ou finalizam dentro da data buscada.
    reservas = ReservaQuarto.objects.filter(
        Q(entrada__range=[entrada-timezone.timedelta(days=1), saida+timezone.timedelta(days=1)])|
        Q(saida__range=[entrada, saida+timezone.timedelta(days=1)])|
        Q(entrada__lte=entrada,saida__gte=saida)
    )

    # Cria uma lista com a reservas
    reservas = CriarListaReservas(reservas)

    # Busca todos os apartamento cadastrados
    apartamentos = Quarto.objects.all().order_by("nome")

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
            'id': apartamento.id,
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
                # Colocando informações na celula
                celula = {
                    'pk': reserva['pk'],
                    'data': data.strftime("%d-%m-%Y-%p"),
                    'quarto':reserva["quarto"],
                    'status': reserva["status"],
                    'status_ap': reserva["status_ap"],
                    'checkin': reserva['checkin'],
                    'checkout': reserva['checkout'],
                }
                print("Check out")
                print(reserva['checkout'])
                print(reserva['status'])

                celula['texto'] = "<h4>"+reserva["cliente"]+"</h4>"

                hoje = datetime.strptime(timezone.now().strftime("%d/%m/%Y"), "%d/%m/%Y")
                hoje = hoje.replace(tzinfo=pytz.UTC)


                if reserva["checkin"] == None and reserva["entrada"]>=hoje:
                    celula['texto'] += ('</h4>'+
                    '<a class="btn btn-success btn-xs" data-toggle="modal" data-target="#checkin-modal" data-whatever='+str(reserva["pk"])+'> Check in</a>')
                elif reserva["checkin"] != None and reserva["checkout"] == None:
                    celula['texto'] += ('</h4>'+
                    '<a class="btn btn-success btn-xs" data-toggle="modal" data-target="#checkout-modal" data-whatever='+str(reserva["pk"])+'> Check out</a>')



                celula['texto'] += ' <a class="btn btn-warning btn-xs" data-toggle="modal" data-target="#reserva-modal" data-whatever='+str(reserva["pk"])+'>Visualizar</a>'
                # A entrada da reserva bate com a data da celula
                if reserva["entrada"].strftime("%d-%m-%Y-%p") == data.strftime("%d-%m-%Y-%p"):


                    # Se a reserva for realmente para aquele apartamento
                    if str(reserva["quarto"]) == str(apartamento.nome):
                        # criando com a reserva.
                        celula['turnos'] = calcula_turnos(reserva["entrada"],reserva["saida"])

                        if reserva["saida"] > saida+timezone.timedelta(days=1):
                            celula["turnos"] = calcula_turnos(reserva["entrada"], saida+timezone.timedelta(days=1))

                        # Marca que achou uma reserva para esta celula
                        achou = True
                        reservas = RemoveReservaLista(reservas, reserva)
                        break



                if not(achou):

                    if reserva["entrada"] < entrada:
                        if reserva["quarto"] == apartamento.nome:
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
                    'checkout':None,
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

def criar_reserva(request):
    data = request.GET.get('data', None)
    ap = request.GET.get('ap', None)
    forms = ReservaForm()
    if data and ap:
        context = {
            'data':data,
            'apartamento':ap,
            'forms':forms,
        }
        return render(request, 'hotel/criar_reserva.html', context)

    return HttpResponseRedirect('/hotel/')


def reserva_ajax(request):

    pk = request.GET.get('pk', None)
    reserva = get_object_or_404(ReservaQuarto, pk=pk)
    print("Reserva ajax: " + str(reserva.reserva.cliente))
    # Montando resultados
    data = {}

    data['pk'] = reserva.pk
    data['reserva'] = reserva.reserva.data_reserva.strftime("%d/%m/%Y %p")
    data['reserva_pk'] = reserva.reserva.pk
    data['cliente_pk'] = reserva.reserva.cliente.pk
    data['cliente'] = reserva.reserva.cliente.nome
    data['quarto'] = reserva.quarto.nome
    data['entrada'] = reserva.entrada.strftime("%d/%m/%Y %p")
    data['saida'] = reserva.saida.strftime("%d/%m/%Y %p")
    data['qtd_adultos'] = reserva.qtd_adultos
    data['qtd_crianca'] = reserva.qtd_crianca
    print("Check in: "+str(reserva.checkin))
    data['checkin'] = reserva.checkin.strftime("%d/%m/%Y %H:%M") if (reserva.checkin is not None) else ''
    data['checkout'] = reserva.checkout.strftime("%d/%m/%Y %H:%M") if (reserva.checkout is not None) else ''
    custo = localize(reserva.custo)
    data['custo'] = str(custo)
    data['falta_pagar'] = str(custo)


    return HttpResponse(
        json.dumps(data),
        content_type="applications/json"
    )


def lista_reservas(request, data=None):

        erro = ''
        if request.session.get('erro') is not None:
            erro = request.session.get('erro', None)
            request.session['erro'] = None


        if request.method == "POST":
            data = request.POST.get('data')
            dia = datetime.strptime(data, "%d/%m/%Y")

        if data == None:
            # print(timezone.now())
            dia = datetime.strptime(timezone.now().strftime("%d/%m/%Y"), "%d/%m/%Y")
            # dia = timezone.now().strftime("%d/%m/%Y")

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
            'erro': erro,
            # 'quartos' : quartos,
            # 'reservas_quartos': reservas_quartos,
            'tabela': tabela,
        }
        return render(request, 'hotel/lista_hotel.html', context)

def apartamento(request, pk):
    "Mostra as informações do apartamento"
    apartamento = get_object_or_404(Quarto, pk=pk)
    pax = apartamento.PaxTotal()
    context = {
        'apartamento': apartamento,
        'pax': pax,
    }

    return render(request, 'hotel/apartamento.html', context)

def editar_apartamento(request, pk):
    "Editar apartamento"
    apartamento = get_object_or_404(Quarto, pk=pk)

    if request.method == "POST":
        forms = QuartoForm(
            request.POST,
            request.FILES,
            instance=apartamento,
            prefix="main"
        )
        if forms.is_valid():
            forms = forms.save()
            # forms.save()
            return HttpResponseRedirect('/hotel/')
    else:

        forms = QuartoForm(
        instance=apartamento,
        prefix='main')
    context = {
        'apartamento':apartamento,
        'forms': forms,
    }
    return render(request, 'hotel/editar_apartamento.html', context)

def checkin_apartamento(request, pk):
    reserva = get_object_or_404(ReservaQuarto, pk=pk)

    if reserva.set_checkin():
        reserva.save()
        return HttpResponseRedirect('/hotel/')
    else:
        erro = "Não foi possivel fazer check in!"
        # erro = quote(erro)
        request.session['erro'] = erro
        return HttpResponseRedirect('/hotel/')



def checkout_apartamento(request, pk):
    reserva = get_object_or_404(ReservaQuarto, pk=pk)
    if reserva.set_checkout():
        reserva.save()
        return HttpResponseRedirect('/hotel/')
    else:
        erro = "Não foi possivel fazer check out!"
        # erro = quote(erro)
        request.session['erro'] = erro
        return HttpResponseRedirect('/hotel/')
