from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Usuario
from rest_framework.generics import ( CreateAPIView, RetrieveUpdateAPIView, 
                                     UpdateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, 
                                     DestroyAPIView) # GenericAPIView
from .serializers import usuarioSerializer, userSerializer, userUpdateSerializer #importamos la clase del serializador del archive serializer.py, en este caso la de usuarioSerializer

from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
# Create your views here.

#@permission_classes((AllowAny, )) 
class usuarioListApi(ListAPIView):  #creamos a lista que va a mostrar la API mediante el llamado en la URL
    serializer_class = usuarioSerializer  #tomamos el modelo serializado
    queryset = 	Usuario.objects.all().order_by('cedula') #Hacemos la consulta de usuarios, donde muestra todos los datos pero los organiza por orden de cedula.
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class oneUsuarioListApi(ListAPIView):  #creamos a lista que va a mostrar la API mediante el llamado en la URL
    serializer_class = usuarioSerializer  #tomamos el modelo serializado
    print("***************")
    def get_queryset(self):
        #cedula="1018468"
        cedula = self.kwargs['cedula'] #Permite obtener el parametro enviado desde la url
        print("***************"+cedula)
        queryset = Usuario.objects.filter(cedula=cedula)
        return queryset

class userListApi(ListAPIView):  #creamos a lista que va a mostrar la API mediante el llamado en la URL
    serializer_class = userSerializer  #tomamos el modelo serializado
    queryset = 	User.objects.all()

class usuarioCreateApi(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = usuarioSerializer

class userCreateApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer

class userUpdateApi(UpdateAPIView):
    serializer_class = userUpdateSerializer
    queryset = Usuario.objects.all()
    '''
    def update(self, request, *args, **Kwargs):
        instance = self.get_object() #Obtener la instancia del objeto Usuario a actualizar
        user_data = request.data.get('pk',{}) #Obtener los datos del usuario de la solicitud
        # Crear una instancia del serializador userSerializer con los datos del usuario y la instancia existente
        user_serializer = userSerializer(instance, data=user_data, partial=True)

        if user_serializer.is_valid():
            user_serializer.save()

        # Obtener una instancia del serializador usuarioSerializer para el objeto Usuario actualizado
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        # Validar el serializador y realizar la actualización
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        # Devolver la respuesta con los datos actualizados del serializador
        return Response(serializer.data)
    '''
