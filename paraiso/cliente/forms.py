from django import forms
from django.forms import inlineformset_factory

from .models import Cliente, Contato, Documento
from tags.models import aplicar_tags, tags_para_objeto

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        exclude = {'data_criacao'}
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_pessoa':forms.Select(attrs={'class':'form-control'}),
        }

    tags = forms.CharField(max_length=30, required=False)

    def __init__(self, *args, **kwargs):

        super(ClienteForm, self).__init__(*args, **kwargs)

        if self.instance.id:
            self.initial['tags'] = tags_para_objeto(self.instance)

    def save(self, *args, **kwargs):
        cliente = super(ClienteForm, self).save(*args, **kwargs)
        # Forçando o save para criar um id caso seja um novo cliente
        cliente.save()
        aplicar_tags(cliente, self.cleaned_data['tags'])

        return cliente

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

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        exclude = ['cliente']
        widgets = {
            'tipo_documento':forms.Select(attrs={'class':'form-control tipo_documento'}),
            'documento':forms.TextInput(attrs={'class':'form-control contato',
                                                'size':24}),
            'descricao':forms.Textarea(attrs={'class':'form-control',
                                                'rows':'3',
                                                'placeholder':'Descrição'}),
        }
