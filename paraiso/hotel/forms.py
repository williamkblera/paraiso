from django import forms
from django.forms import inlineformset_factory

from cliente.models import Cliente
from .models import tipo_quarto, Quarto, Reserva, ReservaQuarto, ReservaPagamento

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        exclude = {'data_reserva'}

        cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())

class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        exclude = {}

        widgets = {
            'nome':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nome',
                'size':'24'}),
            'tipo_quarto': forms.Select(attrs={
                'class':'form-control'}),
            'descricao': forms.Textarea(attrs={
                'class':'form-control',
                'rows': '3',
                'placeholder': 'Descrição'}),
                'cama_casal': forms.NumberInput(attrs={
                    'class':'form-control',
                }),
                'cama_solteiro': forms.NumberInput(attrs={
                    'class':'form-control',
                }),
                'status': forms.Select(attrs={
                    'class':'form-control',
                })

        }
