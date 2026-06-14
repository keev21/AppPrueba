from django.urls import path
from . import views

urlpatterns = [
    # Ruta para listar los tickets
    path('', views.TicketListView.as_view(), name='lista_tickets'),
    # Ruta para crear un nuevo ticket
   path('/nuevo',views.TicketCreateView.as_view(), name='crear_ticket'),
    
]
