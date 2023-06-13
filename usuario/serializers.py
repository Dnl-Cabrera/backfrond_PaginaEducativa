#importamos el modelo creado.
from .models import Usuario
#import the model users from django, that model is used in the Usuario model.
from django.contrib.auth.models import User

#Se importan las librerias necesarias para realizar la APIREST mediante serialización.
#Esta serialización permite identificar el modelo que se va a consultar y la tabla que se va a enviar mediante
#la consulta por medio de la URL.
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ( SerializerMethodField )
from rest_framework import serializers

#This import is for can add the news register a permission group for do modification en los models, for example
#can view the list of users or can edit or register some users.
from django.contrib.auth.models import Group


#Create the new model, but this model is relationship with the model users from django.
#This model is created for used in the class usuarioSerializer for show de items from the table user from django.
class userSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ['pk', 'username', 'password'] #in this case only show the fields username and password from user model. However, this model has many fields, for example, first_name and last_name.
		#fields =  '__all__' #We can use this parameter for see the name of each field the user table using the url for createuser
        
	
from rest_framework.serializers import PrimaryKeyRelatedField

class usuarioUpdateSerializer(ModelSerializer): 
	#id_users = userSerializer(many=False)
	class Meta:
		#in this class we need show the fields relationship with de model user, this model is created by django"
        #With this id_user, in the views we can see the fields in the model user from django for create a new user.
        #This creations create the user in the table users, from django, and usuario, model create by our.
		model = Usuario # model.ty.. Es el nombre del modelo importado, ejemplo Academico. 
		fields = '__all__'

class userUpdateSerializer(ModelSerializer):
	id_userss = usuarioUpdateSerializer(many=False)
	class Meta:
		model = User
		fields = '__all__'

class usuarioSerializer(ModelSerializer): 

	#For see the fields of the user model from django, we need add the description from field used in the model usuario.
    #in this case id_users is foreing key from user.
	id_users = userSerializer(many=False)
	class Meta:
		#in this class we need show the fields relationship with de model user, this model is created by django"
        #With this id_user, in the views we can see the fields in the model user from django for create a new user.
        #This creations create the user in the table users, from django, and usuario, model create by our.
		model = Usuario # model.ty.. Es el nombre del modelo importado, ejemplo Academico. 
		fields = '__all__'

	# This a method necesary for create a usuario.
	# This method relation with user, its allow create a user in the table user of django
	# preguntar como funciona este metodo.
	def create(self, validated_data):
		#Como funciona
		user_data = validated_data.pop('id_users')
		user = User.objects.create(**user_data)
		group_name = "Coordinadores"  # Reemplaza "nombre_del_grupo" con el nombre del grupo al que deseas asignar al usuario
		
		try:
			group = Group.objects.get(name=group_name)
		except Group.DoesNotExist:
			# Manejar el caso si el grupo no existe
			# Por ejemplo, lanzar una excepción o asignar a un grupo predeterminado
			return None
		
		user.groups.add(group)
		usuario = Usuario.objects.create(id_users=user, **validated_data)
		return usuario
	
##Preguntar
#Como eliminar en cascada
#Como funciona la funcion create
#como actualizar un dato.
#