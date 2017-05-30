from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.forms.models import inlineformset_factory
from django.http.response import HttpResponseRedirect

from .models import Cliente, Contato
from .forms import ClienteForm, ContatoForm

def lista_clientes(request):
    # clientes = Cliente.objects.all()
    clientes = Cliente.objects.all().order_by('nome')
    return render(request, 'cliente/lista_clientes.html', {'clientes': clientes})

def cliente_detalhes(request, pk):
    # clientes = Cliente.objects.all()
    # clientes = Cliente.objects.all().order_by('nome')
    cliente = get_object_or_404(Cliente, pk=pk)
    contatos = Contato.objects.filter(cliente=cliente)
    return render(request,'cliente/cliente.html', {'cliente': cliente, 'contatos':contatos})


def novo_cliente(request):
    clienteform = Cliente()
    contato_cliente_formset = inlineformset_factory(
        Cliente,
        Contato,
        form=ContatoForm,
        extra=1,
        can_delete=False,
        min_num=1,
        validate_min=True
    )

    if request.method == "POST":
        forms = ClienteForm(
            request.POST,
            request.FILES,
            instance=clienteform,
            prefix='main'
        )
        formset = contato_cliente_formset(
            request.POST,
            request.FILES,
            instance=clienteform,
            prefix='product'
        )

        if forms.is_valid() and formset.is_valid():
            forms = forms.save(commit=False)
            forms.save()
            formset.save()
            return HttpResponseRedirect('/')

    else:
        forms = ClienteForm(
            instance=clienteform,
            prefix='main'
        )
        formset = contato_cliente_formset(
            instance=clienteform,
            prefix='product'
        )

    context = {
        'forms':forms,
        'formset': formset,
    }

    return render(request, 'cliente/novo_cliente.html', context)
