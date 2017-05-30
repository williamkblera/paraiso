from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_reservas, name='reservas'),
    url(r'reserva/(?P<pk>[0-9]+)/$', views.reserva, name="reserva"),
]
