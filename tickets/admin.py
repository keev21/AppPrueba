from django.contrib import admin
from .models import Tecnico, Ticket

# Configuraciones opcionales para ver más detalles en las tablas del admin
@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'especialidad')
    search_fields = ('nombre', 'email')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'tecnico', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')
    