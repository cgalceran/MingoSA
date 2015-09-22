from .models import Cliente
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class ClienteList(ListView):
    model = Cliente

class ClienteCreate(CreateView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')
    fields = ['Nombre', 'RazonSocial', 'tratamientoimpositivo']

class ClienteUpdate(UpdateView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')
    fields = ['Nombre', 'RazonSocial', 'tratamientoimpositivo']

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')