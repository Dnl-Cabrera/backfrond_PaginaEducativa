from django.contrib import admin

from .models import *

# Register your models here.

'''
from .models import Torre,Apartamento
#Ejemplo que se utilizo en la presentación
admin.site.register(Torre)
admin.site.register(Apartamento)
'''

admin.site.register(Grado)
admin.site.register(Area)
admin.site.register(Asignatura)
admin.site.register(Cursos)
admin.site.register(Matriculados_estudiante)
admin.site.register(Carga_horaria)
admin.site.register(Notas_estudiantes_curso)