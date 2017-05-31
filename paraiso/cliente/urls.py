from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^cliente/novo/$', views.novo_cliente, name='novo_cliente'),
    url(r'^editar/(?P<pk>[0-9]+)/$', views.editar_cliente, name='editar_cliente'),
    url(r'^cliente/(?P<pk>[0-9]+)/$', views.cliente_detalhes, name='cliente'),
    url(r'^del/(?P<pk>[0-9]+)/$', views.deletar_cliente, name='deletar_cliente'),
    url(r'^$', views.lista_clientes, name='lista_clientes'),

]
