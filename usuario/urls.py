from django.urls import re_path, path
#Importamos la vista creada para mostrar el json y vincularla con una url.
from .views import usuarioListApi, usuarioCreateApi,userCreateApi, userListApi, userUpdateApi, oneUsuarioListApi 

app_name = 'usuario' # asignamos el nomobre de la startapp
urlpatterns = [
    #path es una forma mas sencilla de enviar parametros por url
    #path es para versiones mas recientes, y re_path es para versiones mas viejas.
    path('onegetuser/<str:cedula>', oneUsuarioListApi.as_view(), name="onegetuser"),
    #Estamos agregando la url para que se visite desde la url de la carpeta raiz que se agrego en urls.py de paginaEducativa
    #en dicho archivo esta la extensión usuario.
    #En el presente archivo se esta agregando una extension a usuario que se llama getusers.
    re_path(r"^getusers$", usuarioListApi.as_view(), name="getusers"), 
    re_path(r"^createuser$", usuarioCreateApi.as_view(), name="createuser"), 
    #urls relationship with the model user from django.
    re_path(r"^getusersroot$", userListApi.as_view(), name="getusersroot"), 
    re_path(r"^createuserroot$", userCreateApi.as_view(), name="createuserroot"), 
    path('updateuser/<int:pk>', userUpdateApi.as_view(), name="updateuser")
]