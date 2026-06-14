from django.shortcuts import render
from django.views.generic import ListView, CreateView
#redireccionamiento lazy
from django.urls import reverse_lazy
from .models import Ticket

#ver lista de tickets
#el listview se encarga de obtener los datos de la base de datos y pasarlos al template para que se muestren en pantalla. Es una vista genérica que facilita la creación de vistas basadas en listas de objetos.
class TicketListView(ListView):
    model = Ticket
    template_name = 'tickets/lista_tickets.html' # El archivo HTML que usará
    context_object_name = 'tickets'

class TicketCreateView(CreateView):
    model = Ticket
    template_name = 'tickets/form_ticket.html' # El HTML del formulario
    fields = ['titulo', 'descripcion', 'estado', 'tecnico'] # Los campos que queremos en el formulario
    success_url = reverse_lazy('lista_tickets') # A dónde va el usuario tras guardar con éxito