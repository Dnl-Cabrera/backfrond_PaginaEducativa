from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Usuario
from rest_framework.generics import ( CreateAPIView, RetrieveUpdateAPIView, 
                                     UpdateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, 
                                     DestroyAPIView) # GenericAPIView
from .serializers import usuarioSerializer, userSerializer #importamos la clase del serializador del archive serializer.py, en este caso la de usuarioSerializer

# Create your views here.

#@permission_classes((AllowAny, )) 
class usuarioListApi(ListAPIView):  #creamos a lista que va a mostrar la API mediante el llamado en la URL
    serializer_class = usuarioSerializer  #tomamos el modelo serializado
    queryset = 	Usuario.objects.all().order_by('cedula') #Hacemos la consulta de usuarios, donde muestra todos los datos pero los organiza por orden de cedula.

class userListApi(ListAPIView):  #creamos a lista que va a mostrar la API mediante el llamado en la URL
    serializer_class = userSerializer  #tomamos el modelo serializado
    queryset = 	User.objects.all()

class usuarioCreateApi(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = usuarioSerializer

class userCreateApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer

