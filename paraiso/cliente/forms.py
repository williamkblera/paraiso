from django import forms
from django.forms import inlineformset_factory

from .models import Cliente, Contato

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        exclude = {'data_criacao'}
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_pessoa':forms.Select(attrs={'class':'form-control'}),
        }

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ['cliente']
        widgets = {
            'tipo_contato':forms.Select(attrs={'class':'form-control tipo_contato'}),
            'contato':forms.TextInput(attrs={'class':'form-control contato',
                                                'size':'24'}),
            'descricao':forms.Textarea(attrs={'class':'form-control',
                                                'rows':'3',
                                                'placeholder': 'Descrição'}),
        }
