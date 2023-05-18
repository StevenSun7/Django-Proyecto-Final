from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class contacto (models.Model):
    contacto = models.IntegerField (primary_key= True)
    apellido = models.CharField (max_length= 100)
    nombre = models.CharField (max_length= 100)
    email = models.EmailField (max_length= 20)    
    telefono = models.CharField (max_length= 100)
    consulta = models.BooleanField (default= False)
    comentario = models.TextField (blank=True)
    
    def __str__(self):
        return self.nombre + 'Registrado con exito'