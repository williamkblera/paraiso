from django.forms.models import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import OrderForm, ItemOrderForm
from .models import Order, ItemOrder

def order(request):
    order_forms = Order()
    item_order_formset = inlineformset_factory(
        Order,
        ItemOrder,
        form=ItemOrderForm,
        extra=1,
        can_delete=False,
        min_num=1,
        validate_min=True
    )

    if request.method == "POST":
        forms = OrderForm(
            request.POST,
            request.FILES,
            instance=order_forms,
            prefix='main'
        )
        formset = item_order_formset(
            request.POST,
            request.FILES,
            instance=order_forms,
            prefix='product'
        )

        if forms.is_valid() and formset.is_valid():
            forms = forms.save(commit=False)
            forms.save()
            formset.save()
            return HttpResponseRedirect('/teste/')

    else:
        forms = OrderForm(
            instance=order_forms,
            prefix='main'
        )
        formset = item_order_formset(
            instance=order_forms,
            prefix='product'
        )

    context = {
        'forms': forms,
        'formset' : formset,
    }

    return render(request, 'teste/order.html', context)
