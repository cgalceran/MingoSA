"""administrador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from views import clientesview


urlpatterns = [
    url(r'', 'clientes.views.clientesview'),
    
    url(r'/new/', 'clientes.views.new'),
    
    url(r'/add/', 'clientes.views.add'),
    url(r'/edit/', 'clientes.views.edit'),
    url(r'/update/', 'clientes.views.update'),
    url(r'/delete/', 'clientes.views.delete'),
    url(r'/edit/(?P<id>\d+)', 'clientes.views.edit'),
    url(r'/update/(?P<id>\d+)', 'clientes.views.update'),
    url(r'/delete/(?P<id>\d+)', 'clientes.views.delete')  
]

"""

from django.conf.urls import patterns, url

from clientes import views

urlpatterns = patterns('',
  url(r'^', views.ClienteList.as_view(), name='cliente_list'),
  url(r'^new$', views.ClienteCreate.as_view(), name='cliente_new'),
  url(r'^edit/(?P<pk>\d+)$', views.ClienteUpdate.as_view(), name='cliente_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.ClienteDelete.as_view(), name='cliente_delete'),
)

