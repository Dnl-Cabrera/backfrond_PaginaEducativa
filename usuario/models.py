from django.db import models
#Se esta importando el modelo de usuarios que genera Django.
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    id_users=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True) #Se crea la relacion con la tabla User, el cual debe ser uno a uno. 
    cedula=models.CharField(max_length=50,default='',unique=True)
    nombre=models.CharField(max_length=50,default='')
    apellido=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,default='')
    telefono=models.CharField(max_length=50,default='')
    estado_usuario=models.CharField(max_length=50,default='Activo')
    fecha_creacion=models.DateField(max_length=50,auto_now_add=True)
    #En este caso no aplica por que no se esta haciendo referencia.
    def __str__(self):
        return self.cedula