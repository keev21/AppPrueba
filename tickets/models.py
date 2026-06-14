from django.db import models

class Tecnico(models.Model):
    nombre=models.CharField(max_length=100)
    especialidad=models.CharField(max_length=100, blank=True, null=True)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
    
class Ticket(models.Model):
    ESTADOS_OPCIONES = [
        ('abierto', 'Abierto'),
        ('en_progreso', 'En Progreso'),
        ('resuelto', 'Resuelto'),
    ]
    titulo=models.CharField(max_length=200)
    descripcion=models.TextField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    estado=models.CharField(max_length=20, choices=ESTADOS_OPCIONES, default='abierto')
   # PROTECT: Si el técnico tiene un ticket, Django impedirá borrar al técnico.
    # blank=False y null=False: Obliga a que todo ticket tenga un técnico asignado sí o sí.
    tecnico = models.ForeignKey(Tecnico, on_delete=models.PROTECT, related_name='tickets', blank=False, null=False)

    def __str__(self):
        return f"{self.titulo} ({self.estado})"
    
    
