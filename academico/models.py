from django.db import models
from usuario.models import Usuario
from matriculas.models import Matricula

# Create your models here.
'''
Ejemplo que se utilizo en la presentación.
from personal.models import Domicilio

class Torre(models.Model):
    #id_domicilio=models.ForeignKey(Domicilio,on_delete=models.CASCADE)
    #agregar el id no es necesario, django lo crea.
    Nombre=models.CharField(max_length=50,default='')
    id_Domicilio=models.ForeignKey(Domicilio,on_delete=models.CASCADE)

class Apartamento(models.Model):
    Nombre=models.CharField(max_length=50,default='')
'''
class Grado(models.Model):
    grado=models.CharField(max_length=50,default='')
    estado_grado=models.CharField(max_length=50,default='Activo')
    fecha_creacion=models.DateField(max_length=50,auto_now_add=True)
    def __str__(self):
        return self.grado
    
class Area(models.Model):
    id_usuario_jefe_area=models.OneToOneField(Usuario,on_delete=models.CASCADE,primary_key=True) #Se esta creando una relacion uno a uno, Preguntar como funciona el primary Key  
    area=models.CharField(max_length=50,default='')
    estado_area=models.CharField(max_length=50,default='Activo')
    fecha_creacion=models.DateField(max_length=50,auto_now_add=True)
    def __str__(self):
        return self.area

class Asignatura(models.Model):
    id_grado=models.ForeignKey(Grado,on_delete=models.CASCADE)
    id_Area=models.ForeignKey(Area,on_delete=models.CASCADE)
    asignatura=models.CharField(max_length=50,default='')
    estado_asignatura=models.CharField(max_length=50,default='Activo')
    fecha_creacion=models.DateField(max_length=50,auto_now_add=True)
    def __str__(self):
        return self.asignatura

class Cursos(models.Model):
    #id_lista_estudiantes=models.ForeignKey(Lista_estudiantes,on_delete=models.CASCADE)
    id_grado=models.ForeignKey(Grado,on_delete=models.CASCADE)
    id_usuario_director_curso=models.OneToOneField(Usuario,on_delete=models.CASCADE,primary_key=True)
    curso=models.CharField(max_length=50,default='')
    estado_curso=models.CharField(max_length=50,default='Activo')
    fecha_creacion=models.DateField(max_length=50,auto_now_add=True)
    def __str__(self):
        return self.curso

class Matriculados_estudiante(models.Model):
    id_matricula=models.ForeignKey(Matricula,on_delete=models.CASCADE)
    id_curso=models.ForeignKey(Cursos,on_delete=models.CASCADE)
    #id_usuario_director_curso=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    #id_usuario_director_curso=models.OneToOneField(Usuario,on_delete=models.CASCADE,primary_key=True) #Se esta creando una relacion uno a uno, Preguntar como funciona el primary Key  
    estado_lista_estudiante=models.CharField(max_length=50,default='Activo')
    fecha_creacion=models.DateField(max_length=50,auto_now_add=True)
    def __str__(self):
        return self.id_curso.curso

class Carga_horaria(models.Model):
    
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE)
    id_curso=models.ForeignKey(Cursos,on_delete=models.CASCADE)
    estado_carga_horaria=models.CharField(max_length=50,default='Activo')
    fecha_creacion=models.DateField(max_length=50,auto_now_add=True)
    class Meta:
        unique_together = (('id_asignatura', 'id_curso'),)
        
    def __str__(self):
        #Si dejamos los tres items se puede, sin embargo, al momento de cargar los datos en notas_estudiantes, presentaria un error
        #debido a que la interfaz de bases de datos de django no puede mostrar tuplas.
        #return self.id_usuario.cedula#, self.id_asignatura.asignatura,self.id_curso.curso
        
        #forma de mostrar los tres elementos al tiempo
        template= '{0.id_usuario.cedula} {0.id_asignatura.asignatura} {0.id_curso.curso}'
        return template.format(self)
        

class Notas_estudiantes_curso(models.Model):
    id_matriculados_estudiante_curso=models.ForeignKey(Matriculados_estudiante,on_delete=models.CASCADE)
    id_asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE)
    id_carga_horaria=models.ForeignKey(Carga_horaria,on_delete=models.CASCADE)
    Nota=models.CharField(max_length=50,default='')
    fecha_creacion=models.DateField(max_length=50,auto_now_add=True)
    def __str__(self):
        return self.Nota


    