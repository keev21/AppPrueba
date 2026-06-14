from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#redireccionamiento lazy
from django.urls import reverse_lazy
from .models import Ticket, Tecnico
from django.db.models import PROTECT, ProtectedError # <-- Importa ProtectedError
from django.contrib import messages # <-- Importa el sistema de mensajes
from django.shortcuts import redirect # <-- Importa redirect

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

class TicketUpdateView(UpdateView):
    model= Ticket
    template_name = 'tickets/form_ticket.html'
    fields = ['titulo', 'descripcion', 'estado', 'tecnico']
    success_url = reverse_lazy('lista_tickets')

class TicketDeleteView(DeleteView):
    model= Ticket
    template_name = 'tickets/confirmar_borrado.html'
    success_url = reverse_lazy('lista_tickets')

class TecnicoListView(ListView):
    model= Tecnico
    template_name = 'tickets/lista_tecnicos.html'
    context_object_name = 'tecnicos'

class TecnicoCreateView(CreateView):
    model = Tecnico
    template_name = 'tickets/form_tecnico.html'
    fields = ['nombre', 'especialidad', 'email']
    success_url = reverse_lazy('lista_tecnicos')

class TecnicoUpdateView(UpdateView):
    model= Tecnico
    template_name = 'tickets/form_tecnico.html'
    fields = ['nombre', 'especialidad', 'email']
    success_url = reverse_lazy('lista_tecnicos')

class TecnicoDeleteView(DeleteView):
    model = Tecnico
    template_name = 'tickets/confirmar_borrado_tecnico.html'
    success_url = reverse_lazy('lista_tecnicos')

    # Cambiamos "delete" por "post", que es el que recibe el clic del formulario
    def post(self, request, *args, **kwargs):
        if self.get_object().tickets.exists(): # ¿Tiene tickets asignados en Postgres?
            messages.error(request, "No se puede borrar: este técnico tiene tickets asignados.")
            return redirect('lista_tecnicos')
        return super().post(request, *args, **kwargs) # Si no tiene, borra normal
    
    