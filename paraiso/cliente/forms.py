from django import forms
from django.forms import inlineformset_factory

from .models import Cliente, Contato

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        exclude = {'data_criacao'}

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ['cliente']
