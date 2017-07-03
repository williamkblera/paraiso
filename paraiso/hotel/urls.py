from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_reservas, name='reservas'),
    url(r'reserva/(?P<pk>[0-9]+)/$', views.reserva, name="reserva"),
    url(r'reserva_ajax/$', views.reserva_ajax, name="reserva_ajax"),
    url(r'apartamento/editar/(?P<pk>[0-9]+)/$', views.editar_apartamento, name='editar_apartamento'),
    url(r'reserva/criar/$', views.criar_reserva, name="criar_reserva"),
    url(r'apartamento/checkin/(?P<pk>[0-9]+)/$', views.checkin_apartamento, name='checkin_apartamento'),
    url(r'apartamento/checkout/(?P<pk>[0-9]+)/$', views.checkout_apartamento, name='checkout_apartamento'),
    url(r'apartamento/(?P<pk>[0-9]+)/$', views.apartamento, name="apartamento"),

]
