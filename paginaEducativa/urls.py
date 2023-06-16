"""
URL configuration for paginaEducativa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings

from dj_rest_auth.registration.views import RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("usuario/", include("usuario.urls", namespace="usuario")), #En este caso estamos agregando las urls que estan en la startapp de usuario para poderlas consultar.
    #en este caso la direccion es usuario y lo va a ir a buscar en la startapp usuario en el archivo urls.py
    #Se debe importar la libreria include
    path('dj-rest-auth/', include('dj_rest_auth.urls')),#Import the path for the template from dj_rest for generate the token in the moment the login.
    path('auth/registration/', RegisterView.as_view(), name='rest_register'), #import template for the register user. This path of registration its can make with the serializer for include all fields from usuario models.
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(".well-known", document_root=settings.MEDIA_ROOT)

