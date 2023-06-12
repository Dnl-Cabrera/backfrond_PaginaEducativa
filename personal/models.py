from django.db import models
#Se esta importando el modelo de usuarios que genera Django.
#from django.contrib.auth.models import User
#Estamos importando la tabla usuario de la startapp Usuario que se relaciona con user de django mediante una
#llave foranea.
from usuario.models import Usuario

# Create your models here.

class Pais(models.Model):
    #agregar el id no es necesario, django lo crea.
    pais=models.CharField(max_length=50,default='')
    Continente=models.CharField(max_length=50,default='')
    #Es para que autmaticamenrte muestre el nombre del modelo Pais cuando se haga alguna referencia, ej: en estado que tiene el id_pais.
    def __str__(self):
        return self.pais

class Estado(models.Model):
    id_pais=models.ForeignKey(Pais,on_delete=models.CASCADE)
    estado=models.CharField(max_length=50,default='')
    indicativo=models.CharField(max_length=50,default='')
    fecha_creacion=models.DateField(max_length=50,auto_now_add=True)
    def __str__(self):
        return self.estado

class Ciudad(models.Model):
    id_estado=models.ForeignKey(Estado,on_delete=models.CASCADE)
    ciudad=models.CharField(max_length=50,default='')
    fecha_creacion=models.DateField(max_length=50,auto_now_add=True)
    def __str__(self):
        return self.ciudad

class Domicilio(models.Model):
    id_ciudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE) #Este debe ir relacionado con alguna tabla de Django de usuarios.
    direccion=models.CharField(max_length=50,default='')
    codigo_postal=models.CharField(max_length=50,default='')
    barrio=models.CharField(max_length=50,default='')
    fecha_creacion=models.DateField(max_length=50,auto_now_add=True)
    #En este caso no aplica por que no se esta haciendo referencia.
    def __str__(self):
        return self.direccion

    