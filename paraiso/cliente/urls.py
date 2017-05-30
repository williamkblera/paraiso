from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^cliente/novo/$', views.novo_cliente, name='novo_cliente'),
    url(r'^cliente/(?P<pk>[0-9]+)/$', views.cliente_detalhes, name='cliente'),
    url(r'^$', views.lista_clientes, name='lista_clientes'),

]
