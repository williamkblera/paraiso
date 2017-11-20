from django import forms

from cliente.models import Cliente
from .models import Produto

class ProdutoForm(forms.ModelForm):
    preco = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        localize=True,
        widget=forms.TextInput(attrs={'class':'form-control preco'}),
    )

    class Meta:
        model = Produto
        exclude = {}
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'descricao':forms.Textarea(attrs={'class':'form-control'}),
            'tipo_produto':forms.Select(attrs={'class':'form-control'}),
            #'preco':forms.TextInput(attrs={'class':'form-control preco'}),
            'limite_dia':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        }


class ReservaProdutoForm(forms.ModelForm):
    cliente = forms.ModelMultipleChoiceField(
        queryset=Cliente.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
    )
    data = forms.DateField(
        widget=forms.SelectDateWidget()
    )
    produto = forms.ModelMultipleChoiceField(
        queryset=Produto.objects.all(),
        widget=forms.Select(attrs={"class":'form-control'}),
    )

    class Meta:
        model = Produto
        fields = [
        'cliente',
        'data', 'produto'
        ]
