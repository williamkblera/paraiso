"""paraiso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from paraiso.cliente import views

urlpatterns = [
    url(r'^teste/', include('teste.urls', namespace='teste')),
    url(r'^hotel/', include('hotel.urls', namespace='hotel')),
    url(r'^clientes/', include('cliente.urls', namespace="clientes") ),
    url(r'^produtos/', include('produto.urls', namespace='produtos')),
    url(r'^$', include('core.urls', namespace='core')),
    url(r'^admin/', admin.site.urls),
    url(r'^tags/', include('tags.urls', namespace='tags')),
]
