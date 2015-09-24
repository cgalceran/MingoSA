from .models import Cliente
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy



class ClienteList(ListView):
    model = Cliente

class ClienteCreate(CreateView):
    model = Cliente
    success_url = reverse_lazy('clientes:cliente_list')
    fields = ['Nombre', 'RazonSocial', 'direccionfiscal', 'departamento', 'codigopostal', 'localidad', 'provincia', 'pais',
    'telefono','email','condicionpago', 'cuit', 'ingresosbrutos', 'numerodocumento', 'tipodedocumento', 'enviarcomprobante',
     'percibeiibb', 'percibeiiva', 'tratamientoimpositivo']

class ClienteUpdate(UpdateView):
    model = Cliente
    success_url = reverse_lazy('clientes:cliente_list')
    fields = ['Nombre', 'RazonSocial', 'direccionfiscal', 'departamento', 'codigopostal', 'localidad', 'provincia', 'pais',
    'telefono','email','condicionpago', 'cuit', 'ingresosbrutos', 'numerodocumento', 'tipodedocumento', 'enviarcomprobante',
     'percibeiibb', 'percibeiiva', 'tratamientoimpositivo']

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:cliente_list')    

