from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_produtos, name='lista_produtos'),
    url(r'^produto/(?P<pk>[0-9]+)/$', views.produto_detalhes, name="produto"),
    url(r'^produto/novo/$', views.novo_produto, name="novo_produto"),
    url(r'^del/(?P<pk>[0-9]+)/$', views.deletar_produto, name='deletar_produto'),
    url(r'^editar/(?P<pk>[0-9]+)/$', views.editar_produto, name='editar_produto'),
    url(r'^reserva/$', views.lista_reservas, name='lista_reservas'),
    url(r'^reserva/(?P<pk>[0-9]+)/$', views.reserva_detalhes, name="reserva"),
    url(r'^reserva/del/(?P<pk>[0-9]+)/$', views.deletar_reserva, name="deletar_reserva"),
    url(r'^reserva/nova/$', views.nova_reserva, name="nova_reserva"),
]
