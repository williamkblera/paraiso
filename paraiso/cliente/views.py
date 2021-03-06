from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.forms.models import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.db.models import Q
from django.core.urlresolvers import reverse
from urllib.parse import urlsplit


from .models import Cliente, Contato, Documento
from .forms import ClienteForm, ContatoForm, DocumentoForm

def lista_clientes(request):
    if request.method == "POST":
        busca = request.POST.get('busca')
        if busca == "":
            clientes = Cliente.objects.all().order_by('nome')
        else:
            clientes = Cliente.objects.filter(
                    Q(nome__icontains=busca)|
                    Q(contatos__contato__icontains=busca)|
                    Q(documentos__documento__icontains=busca)
            )
        # clientes = Cliente.objects.filter(nome__icontains=busca)
    else:
        clientes = Cliente.objects.all().order_by('nome')
    return render(request, 'cliente/lista_clientes.html', {'clientes': clientes})

def cliente_detalhes(request, pk):
    # clientes = Cliente.objects.all()
    # clientes = Cliente.objects.all().order_by('nome')
    cliente = get_object_or_404(Cliente, pk=pk)
    contatos = Contato.objects.filter(cliente=cliente)
    documentos = Documento.objects.filter(cliente=cliente)
    context = {
        'cliente': cliente,
        'contatos': contatos,
        'documentos': documentos,
    }
    return render(request,'cliente/cliente.html', context)

def deletar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return HttpResponseRedirect('/clientes/')

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    contatos = Contato.objects.filter(cliente=cliente)
    documentos = Documento.objects.filter(cliente=cliente)

    clienteform = cliente
    contato_cliente_formset = inlineformset_factory(
        Cliente,
        Contato,
        form=ContatoForm,
        extra=1,
        can_delete=True,
        min_num=0,
        # validate_min=True
    )
    documento_cliente_formset = inlineformset_factory(
        Cliente,
        Documento,
        form=DocumentoForm,
        extra=1,
        can_delete=True,
        min_num=0,
        # validate_min=True
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
        documentoformset = documento_cliente_formset(
            request.POST,
            request.FILES,
            instance=clienteform,
            prefix='documentos'
        )

        if forms.is_valid() and formset.is_valid() and documentoformset.is_valid():
            f = forms.save(commit=False)
            f.save()
            forms.save_m2m()
            formset.save()
            documentoformset.save()

            return HttpResponseRedirect('/clientes/')

    else:
        forms = ClienteForm(
            instance=clienteform,
            prefix='main'
        )
        formset = contato_cliente_formset(
            instance=clienteform,
            prefix='product'
        )
        documentoformset = documento_cliente_formset(
            instance=clienteform,
            prefix='documentos'
        )

    context = {
        'cliente':cliente,
        'forms':forms,
        'formset': formset,
        'documentoformset': documentoformset,
    }

    return render(request, 'cliente/editar_cliente.html', context)


def novo_cliente(request):

    redirect_to = ""
    if 'next' in request.GET:
        redirect_to = request.GET['next']
        url = request.META.get('HTTP_REFERER', None) or '/' # pega url do site
        next = "{0.scheme}://{0.netloc}/".format(urlsplit(url))+redirect_to
        print(next)
        redirect_to = next



    clienteform = Cliente()
    contato_cliente_formset = inlineformset_factory(
        Cliente,
        Contato,
        form=ContatoForm,
        extra=1,
        can_delete=False,
        min_num=0,
        # validate_min=True
    )
    documento_cliente_formset = inlineformset_factory(
        Cliente,
        Documento,
        form=DocumentoForm,
        extra=1,
        can_delete=True,
        min_num=0,
        # validate_min=True
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
            prefix='contatos'
        )
        documentoformset = documento_cliente_formset(
            request.POST,
            request.FILES,
            instance=clienteform,
            prefix='documentos'
        )

        if forms.is_valid() and formset.is_valid() and documentoformset.is_valid():
            f = forms.save(commit=False)
            f.save()
            forms.save_m2m()
            formset.save()
            documentoformset.save
            if redirect_to == "":
                return HttpResponseRedirect('/clientes/')
            else:
                #return redirect(redirect_to)
                return HttpResponseRedirect('/clientes/')

    else:
        forms = ClienteForm(
            instance=clienteform,
            prefix='main'
        )
        formset = contato_cliente_formset(
            instance=clienteform,
            prefix='contatos'
        )
        documentoformset = documento_cliente_formset(
            instance=clienteform,
            prefix='documentos'
        )

    context = {
        'forms':forms,
        'formset': formset,
        'documentoformset':documentoformset,
    }

    return render(request, 'cliente/add_cliente.html', context)
