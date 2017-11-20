from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.db.models import Q

from .models import Produto, ReservaProduto
from cliente.models import Cliente
from .forms import ProdutoForm, ReservaProdutoForm

def lista_reservas(request):
    reservas = ReservaProduto.objects.all().exclude(status='O').order_by('-data')

    context = {
        'reservas':reservas,
    }
    return render(request, 'produto/lista_reservas.html', context)

def lista_produtos(request):
    if request.method == "POST":
        busca = request.POST.get('busca')
        if busca == "":
            produtos = Produto.objects.all().order_by('status')
        else:
            produtos = Produto.objects.filter(
                Q(nome__icontains=busca)|
                Q(descricao__icontains=busca)
            )
    else:
        produtos = Produto.objects.all().order_by('status')

    return render(request, 'produto/lista_produtos.html', {'produtos':produtos})

def reserva_detalhes(request, pk):
    reserva = get_object_or_404(ReservaProduto, pk=pk)
    return render(request, 'produto/reserva_produto.html', {'reserva':reserva})

def deletar_reserva(request, pk):
    reserva = get_object_or_404(ReservaProduto, pk=pk)
    reserva.delete()
    return HttpResponseRedirect('/produtos/reserva/')

def nova_reserva(request):
    clientes = Cliente.objects.all().order_by('nome')
    if request.method == "POST":
        busca = request.POST.get('busca')
        if busca == "":
            pass
        else:
            clientes = Cliente.objects.filter(
                    Q(nome__icontains=busca)|
                    Q(contatos__contato__icontains=busca)|
                    Q(documentos__documento__icontains=busca)
            )
            
    context = {

        'clientes':clientes,
    }

    return render(request, 'produto/add_reserva.html', context)

def produto_detalhes(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produto/produto.html', {'produto':produto})


def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    return HttpResponseRedirect('/produtos/')

def novo_produto(request):
    if request.method == "POST":
        forms = ProdutoForm(
            request.POST,
            request.FILES,
            instance=Produto(),
            prefix="main"
        )

        if forms.is_valid():
            forms = forms.save()
            return HttpResponseRedirect('/produtos/')
    else:
        forms = ProdutoForm(
            instance=Produto(),
            prefix='main'
        )

    context = {
        'forms':forms,
    }

    return render(request, 'produto/add_produto.html', context)

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == "POST":
        forms = ProdutoForm(
            request.POST,
            request.FILES,
            instance=produto,
            prefix='main'
        )

        if forms.is_valid():
            forms = forms.save(commit=False)
            forms.save()
            return HttpResponseRedirect('/produtos/')

    else:

        forms = ProdutoForm(
            instance=produto,
            prefix='main'
        )

    context = {
        'produto':produto,
        'forms':forms,
    }

    return render(request, 'produto/editar_produto.html', context)
