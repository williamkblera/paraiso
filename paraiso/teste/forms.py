from django import forms
from .models import Order, ItemOrder

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['date']

class ItemOrderForm(forms.ModelForm):
    class Meta:
        model = ItemOrder
        exclude = ['order']
