from django.contrib import admin
#Aca se importan los modelos que se crearon.
from .models import Pais,Domicilio,Estado,Ciudad
 

# Register your models here.

admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Domicilio)