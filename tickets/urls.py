from django.urls import path
from . import views

urlpatterns = [
    # Ruta para listar los tickets
    path('', views.TicketListView.as_view(), name='lista_tickets'),
    # Ruta para crear un nuevo ticket
   path('/nuevo',views.TicketCreateView.as_view(), name='crear_ticket'),
   path('/editar/<int:pk>/', views.TicketUpdateView.as_view(), name='editar_ticket'),
   path('/borrar/<int:pk>/', views.TicketDeleteView.as_view(), name='borrar_ticket'),
   # Rutas para técnicos
    path('/tecnicos/', views.TecnicoListView.as_view(), name='lista_tecnicos'),
    path('/tecnicos/nuevo', views.TecnicoCreateView.as_view(), name='crear_tecnico'),
    path('/tecnicos/editar/<int:pk>/', views.TecnicoUpdateView.as_view(), name='editar_tecnico'),
    path('/tecnicos/borrar/<int:pk>/', views.TecnicoDeleteView.as_view(), name='borrar_tecnico'),
    
]
